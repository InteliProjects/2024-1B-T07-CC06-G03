from sklearn.cluster import MiniBatchKMeans
from sklearn.neighbors import NearestNeighbors
from haversine import haversine, Unit
import pandas as pd
import numpy as np
import time
import glob
import os


"""
Este módulo é destinado à estipular o número de leituristas nencessários para realizar a leitura da amostra fornecida. Com isso, é realizados as clusterizações da amostra com base nos leituristas e dias de trabalho.
As funções deste módulo são projetadas para trabalhar em conjunto a fim de processar dados de entrada, realizar clusterização inicial para teste do problema do caixeiro viajante (TSP), otimizar rotas diárias e finalmente dividir as rotas por dias específicos. Este processo visa maximizar a eficiência das rotas diárias de leitura de medidores.

Funções Incluídas:
- initial_cluster: Realiza a clusterização inicial dos pontos para identificar agrupamentos viáveis para o teste do TSP.
- calculate_time_between_points: Calcula o tempo estimado de viagem entre dois pontos geográficos dados.
- tsp_nearest_neighbor: Aplica o algoritmo do vizinho mais próximo para determinar a sequência ótima de visitas dentro de uma restrição de tempo.
- cluster_route: Agrupa pontos em clusters baseados na quantidade média de pontos que podem ser visitados em um mês.
- cluster_day: Divide os clusters em dias específicos para garantir uma distribuição equilibrada do trabalho.
- process_data: Coordena a execução das funções acima, lê e processa dados de entrada, e gerencia a saída do processo de otimização.

"""


def initial_cluster(minor_sample):
    """
    Realiza a clusterização inicial dos pontos para testes de TSP.

    Args:
        minor_sample (DataFrame): DataFrame contendo as amostras menores com colunas 'LATITUDE' e 'LONGITUDE'.

    Returns:
        DataFrame: DataFrame atualizado com uma nova coluna 'agrupamento' indicando o cluster de cada ponto.
    """
    minor_sample = minor_sample.sort_values(by=["LATITUDE", "LONGITUDE"]).reset_index(drop=True)
    mbkmeans = MiniBatchKMeans(n_clusters=14, random_state=0, batch_size=100)
    minor_sample['agrupamento'] = mbkmeans.fit_predict(minor_sample[['LATITUDE', 'LONGITUDE']]) + 1
    return minor_sample

def calculate_time_between_points(point1, point2,time_readings, speed=5):
    """
    Calcula o tempo de viagem entre dois pontos usando a fórmula de Haversine.

    Args:
        point1 (tuple): Coordenadas (latitude, longitude) do ponto inicial.
        point2 (tuple): Coordenadas (latitude, longitude) do ponto final.
        speed (float, optional): Velocidade média de viagem em km/h. Default é 5.
        stop_time (float, optional): Tempo de parada em minutos. Default é 1.

    Returns:
        float: Tempo total de viagem entre os dois pontos em horas.
    """
    # Utiliza a distância de haversine para calcular as distâncias
    distance = haversine(point1, point2, unit=Unit.KILOMETERS)
    travel_time = distance / speed
    total_time = travel_time + (time_readings / 60)  # Converte minutos para horas
    return total_time

def tsp_nearest_neighbor(df, time_readings,hours_work):
    """
    Executa o algoritmo de vizinhos mais próximos (Nearest Neighbors) com limite de tempo para percorrer os pontos.

    Args:
        df (DataFrame): DataFrame contendo os pontos com colunas 'LATITUDE' e 'LONGITUDE'.
        time_readings(int): Tempo de leitura realizado em cada ponto
        hours_work (float, optional): Tempo máximo permitido para percorrer os pontos em horas. Defalut é 6

    Returns:
        int: Quantidade de pontos visitados dentro do tempo limite.
    """
    # Inicializa uma lista vazia com os pontos visitados
    visited = []
    current_index = df.index[0]
    total_time = 0

    while True:
        remaining_points = df.drop(visited)
        if remaining_points.empty:
            break
        # Procura o ponto visinho mais próximo dentro dos pontos restante pelos seus valores de coordenada
        nbrs = NearestNeighbors(n_neighbors=1).fit(remaining_points[['LATITUDE', 'LONGITUDE']])
        distances, indices = nbrs.kneighbors([df.loc[current_index][['LATITUDE', 'LONGITUDE']]])
        next_index = remaining_points.iloc[indices[0][0]].name
        # Após a adição, calcula o tempo de percorrimento entre esses pontos
        time_to_next_point = calculate_time_between_points(df.loc[current_index][['LATITUDE', 'LONGITUDE']], df.loc[next_index][['LATITUDE', 'LONGITUDE']],time_readings)
        # Para em caso do tempo total utilizado ser mais do que a restrição permite
        if total_time + time_to_next_point > hours_work:
            break

        visited.append(next_index)
        total_time += time_to_next_point
        current_index = next_index

    return len(visited)

def cluster_route(average_visited_rounded, bigger_sample,total_days):
    """
    Divide os pontos do 'bigger_sample' em clusters com base na capacidade de pontos percorridos mensalmente.

    Args:
        average_visited_rounded (int): Média arredondada de pontos visitados por dia.
        bigger_sample (DataFrame): DataFrame contendo as amostras maiores com colunas 'LATITUDE' e 'LONGITUDE'.
        total_days (int): Número total de dias para percorrer os pontos.
    Returns:
        DataFrame: DataFrame atualizado com uma nova coluna 'rotas' indicando o cluster de cada ponto.
    """
    qtt_month = average_visited_rounded * total_days
    data_size = len(bigger_sample)
    clusters = round(data_size / qtt_month)
    clusters = round(clusters + (clusters * 0.10))

    mbkmeans = MiniBatchKMeans(n_clusters=clusters, random_state=0, batch_size=324, n_init=10)
    bigger_sample['rotas'] = mbkmeans.fit_predict(bigger_sample[['LATITUDE', 'LONGITUDE']]) + 1
    return bigger_sample

def cluster_day(df, n_clusters):
    """
    Divide cada cluster na quantidade de dias para serem percorridos.

    Args:
        df (DataFrame): DataFrame contendo as amostras maiores com a coluna 'rotas'.
        n_clusters (int): Número de clusters (dias) para dividir os pontos.

    Returns:
        DataFrame: DataFrame atualizado com uma nova coluna 'dia' indicando o dia de cada ponto.
    """
    results = pd.DataFrame()
    for rota in df['rotas'].unique():
        subdf = df[df['rotas'] == rota].copy()  # Usar copy para evitar SettingWithCopyWarning
        kmeans = MiniBatchKMeans(n_clusters=n_clusters, random_state=0,batch_size=324, n_init=10)  # Define n_init explicitamente
        subdf['dia'] = kmeans.fit_predict(subdf[['LATITUDE', 'LONGITUDE']]) + 1
        results = pd.concat([results, subdf], ignore_index=True)
    return results

def process_data(time_readings, hours_work,total_days):
    """
    Processa os dados, realizando a leitura dos arquivos CSV, a clusterização inicial,
    os testes de TSP, e a divisão final em rotas e dias.

    Args: 
        time_readings (int): Tempo de leitura realizado em cada ponto.
        hours_work (float, optional): Tempo máximo permitido para percorrer os pontos em horas.
        total_days (int): Número total de dias para percorrer os pontos.

    Returns:
        tuple: DataFrame com a clusterização final e o tempo total de processamento em minutos.
        float: tempo de execução do algoritmo de clusterização
    """
    # Inicializa a verificação do tempo de execução
    start_time = time.time()

    database_path = '../database/*'
    list_of_files = glob.glob(database_path + '.csv')

    # Verifica o ultimo arquivo inserido para ser a amostra a ser clusterizada
    if list_of_files:
        latest_file = max(list_of_files, key=os.path.getctime)
        bigger_sample = pd.read_csv(latest_file)
    else:
        print("Nenhum arquivo CSV encontrado na pasta.")

    minor_sample = pd.read_csv("../database/AMOTRA_MENOR.csv", sep=";")
    minor_sample = initial_cluster(minor_sample)

    # Realiza os testes de TSP nos clusters iniciais, e pega o valor médio de pontos percorridos
    results = {}
    for rota in minor_sample['agrupamento'].unique():
        route_df = minor_sample[minor_sample['agrupamento'] == rota]
        visited_count = tsp_nearest_neighbor(route_df,time_readings,hours_work)
        results[rota] = visited_count
    average_visited = np.mean(list(results.values()))
    average_visited_rounded = round(average_visited)
    amostra_rotas = cluster_route(average_visited_rounded, bigger_sample,total_days)
    bigger_sample_clustering = cluster_day(amostra_rotas, total_days)

    # Finaliza o contador de tempo e converte em minutos
    end_time = time.time()
    total_time = end_time - start_time
    total_minutes_clustering = total_time / 60

    print("Cluster Finalizado!")

    return bigger_sample_clustering, total_minutes_clustering