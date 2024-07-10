from sklearn.cluster import MiniBatchKMeans
import pandas as pd
import time
import glob
import os

"""
Este módulo é projetado para gerenciar a clusterização e simulação de rotas em uma aplicação de otimização de rotas. Ele utiliza o algoritmo MiniBatchKMeans para agrupar pontos geográficos com base em suas coordenadas, o que facilita a divisão das tarefas de campo em rotas diárias eficientes. O objetivo é minimizar o tempo e a distância total percorrida pelos leitores de medidores, distribuindo os pontos de maneira equilibrada ao longo de vários dias.

Funções incluídas:
- cluster: Aplica o MiniBatchKMeans para criar clusters principais baseados em localização. Isso prepara os dados para uma subsequente subdivisão em rotas diárias.
- cluster_routes: Subdivide os clusters principais em rotas diárias, também utilizando o MiniBatchKMeans. Cada sub-cluster representa uma rota que pode ser concluída em um único dia, considerando o tempo e a distância de percurso.
- simulate: Simula o processo de clusterização e geração de rotas, fornecendo uma medida de tempo de execução. Isso ajuda a estimar a eficiência do processo de divisão dos dados em rotas diárias e é útil para ajustar parâmetros antes da implantação real.

"""

def cluster(num_clusters, largest_sample):
    """
    Realiza a clusterização dos dados utilizando o algoritmo MiniBatchKMeans.

    Args:
        num_clusters (int): Número de clusters a serem criados.
        largest_sample (DataFrame): DataFrame contendo as amostras com colunas 'LATITUDE' e 'LONGITUDE'.

    Returns:
        DataFrame: DataFrame atualizado com uma nova coluna 'rotas' indicando o cluster de cada ponto.
    """
    mbkmeans = MiniBatchKMeans(n_clusters=num_clusters, random_state=0, batch_size=100)
    largest_sample = largest_sample.copy()
    largest_sample['rotas'] = mbkmeans.fit_predict(largest_sample[['LATITUDE', 'LONGITUDE']]) + 1
    return largest_sample

def cluster_routes(largest_sample, n_clusters):
    """
    Divide cada cluster em sub-clusters para rotas diárias utilizando MiniBatchKMeans.

    Args:
        largest_sample (DataFrame): DataFrame contendo as amostras com a coluna 'rotas'.
        n_clusters (int): Número de sub-clusters (dias) a serem criados em cada cluster principal.

    Returns:
        DataFrame: DataFrame atualizado com uma nova coluna 'dia' indicando o dia de cada ponto.
    """
    result = pd.DataFrame()
    for route in largest_sample['rotas'].unique():
        largest_subdata = largest_sample[largest_sample['rotas'] == route].copy()
        kmeans = MiniBatchKMeans(n_clusters=n_clusters, random_state=42)
        largest_subdata['dia'] = kmeans.fit_predict(largest_subdata[['LATITUDE', 'LONGITUDE']]) + 1
        result = pd.concat([result, largest_subdata], ignore_index=True)
    return result

def simulate(num_readers,total_days):
    """
    Simula a clusterização dos dados e divide em rotas diárias, medindo o tempo total de processamento.

    Args:
        num_readers (int): Número de clusters principais a serem criados.
        total_days (int): Número total de dias para percorrer os pontos.

    Returns:
        tuple: DataFrame com a clusterização final e o tempo total de processamento em minutos.
    """
    # Inicializa a verificação do tempo de execução
    start_time = time.time()

    database_path = '../database/*'
    list_of_files = glob.glob(database_path + '.csv')

    # Verifica o ultimo arquivo inserido para ser a amostra a ser clusterizada
    if list_of_files:
        latest_file = max(list_of_files, key=os.path.getctime)
        largest_sample = pd.read_csv(latest_file)
    else:
        print("Nenhum arquivo CSV encontrado na pasta.")
        return None, 0

    # Realiza a clusterização inicial e a divisão em rotas diárias
    largest_sample = cluster(num_readers, largest_sample)
    num_days = total_days
    cluster_largest_sample = cluster_routes(largest_sample, num_days)

    # Finaliza o contador de tempo e converte em minutos
    end_time = time.time()
    total_time = end_time - start_time
    total_minutes_simulation = total_time / 60

    return cluster_largest_sample, total_minutes_simulation