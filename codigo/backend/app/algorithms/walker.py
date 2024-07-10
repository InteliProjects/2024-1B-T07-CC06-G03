import json
import time
import numpy as np
from numba import jit
from app.algorithms.automatic import *
from app.algorithms.simulation import *

"""
Este módulo é projetado para otimizar e simular rotas geográficas para operações de campo, utilizando algoritmos de otimização de rota como Nearest Neighbor e 2-opt. Ele integra cálculos de distância geográfica via fórmula de Haversine para determinar a menor rota possível entre pontos, otimizando sequências de visitas para minimizar o tempo e a distância total percorrida.


Funções incluídas:
- haversine_distance: Calcula a distância entre dois pontos geográficos usando a fórmula de Haversine.
- nearest_neighbor: Implementa o algoritmo de vizinho mais próximo para determinar uma sequência inicial de visitas a pontos com base em sua proximidade geográfica.
- two_opt: Aplica o algoritmo de otimização 2-opt para refinar rotas, melhorando a ordem de visita dos pontos para reduzir cruzamentos e retrabalho.
- total_distance: Calcula a distância total de uma rota dada, útil para avaliar a eficiência de diferentes sequências de pontos.
- format_to_json: Converte dados em um formato JSON para exportação, facilitando a utilização dos resultados em outras aplicações ou para visualizações.
- walker: Função central que coordena a execução de algoritmos de roteamento e simulações, fornecendo um tempo total de execução.

Este módulo é essencial para aplicações que requerem logística avançada e planejamento detalhado de rotas, como empresas de serviços de campo, distribuição logística e gestão de infraestrutura urbana.
"""


@jit(nopython=True)
def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calcula a distância de Haversine entre dois pontos geográficos.

    Args:
        lat1 (float): Latitude do primeiro ponto.
        lon1 (float): Longitude do primeiro ponto.
        lat2 (float): Latitude do segundo ponto.
        lon2 (float): Longitude do segundo ponto.

    Returns:
        float: Distância em quilômetros entre os dois pontos.
    """
    R = 6371.0
    dLat = np.radians(lat2 - lat1)
    dLon = np.radians(lon2 - lon1)
    a = (np.sin(dLat / 2) ** 2 +
         np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dLon / 2) ** 2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

@jit(nopython=True)
def nearest_neighbor(points):
    """
    Executa o algoritmo de vizinho mais próximo (Nearest Neighbor) para percorrer os pontos.

    Args:
        points (list): Lista de dicionários contendo as coordenadas dos pontos e seus índices.

    Returns:
        list: Lista de pontos visitados na ordem determinada pelo algoritmo.
    """
    num_points = points.shape[0]
    visited = np.zeros(num_points, dtype=np.bool_)
    order = np.empty(num_points, dtype=np.int32)
    order[0] = 0  # Start at the first point
    visited[0] = True
    current_index = 0

    for i in range(1, num_points):
        min_dist = np.inf
        next_index = 0
        for j in range(num_points):
            if not visited[j]:
                dist = haversine_distance(points[current_index, 0], points[current_index, 1], points[j, 0], points[j, 1])
                if dist < min_dist:
                    min_dist = dist
                    next_index = j
        visited[next_index] = True
        order[i] = next_index
        current_index = next_index

    return order

@jit(nopython=True)
def two_opt(route, points):
    """
    Executa o algoritmo de otimização 2-opt para melhorar a rota e remover cruzamentos.

    Args:
        route (list): Lista de índices que representam a ordem dos pontos na rota atual.
        points (numpy.ndarray): Matriz 2D contendo as coordenadas (latitude e longitude) dos pontos.

    Returns:
        tuple: A rota otimizada e o número de iterações de 2-opt realizadas.
    """
    local_two_opt = 0
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(route) - 1):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # Não inverte vizinhos diretos
                new_route = np.concatenate((route[:i], route[i:j][::-1], route[j:]))
                if total_distance(new_route, points) < total_distance(route, points):
                    route = new_route
                    improvement = True
    local_two_opt += 1
    return route, local_two_opt

@jit(nopython=True)
def total_distance(route, points):
    """
    Calcula a distância total de uma rota.

    Args:
        route (list): Lista de índices que representam a ordem dos pontos na rota.
        points (numpy.ndarray): Matriz 2D contendo as coordenadas (latitude e longitude) dos pontos.

    Returns:
        float: A distância total percorrida na rota em quilômetros.
    """
    total_dist = 0.0
    for i in range(len(route) - 1):
        total_dist += haversine_distance(points[route[i], 0], points[route[i], 1], points[route[i + 1], 0], points[route[i + 1], 1])
    return total_dist

def format_to_json(data, var_name):
    """
    Formata uma lista de dicionários em JSON para ser exportada como um arquivo JavaScript.

    Args:
        data (list): Lista de dicionários contendo os dados a serem exportados.
        var_name (str): Nome da variável que irá armazenar os dados no arquivo JavaScript.

    Returns:
        str: String contendo o JSON formatado com os dados.
    """
    json_str = f"export const {var_name} = [\n"
    for item in data:
        json_str += "    {\n"
        for key, value in item.items():
            if isinstance(value, str):
                json_str += f"        {key}: \"{value}\",\n"
            else:
                json_str += f"        {key}: {value},\n"
        json_str += "    },\n"
    json_str += "];\n"
    return json_str

def walker(select_algo, readers, time_readings, hours_work,total_days):
    """
    Função principal que executa o algoritmo de percorrer os pontos na base de dados, iterando por rota e dias.

    Args:
        select_algo (int): Algoritmo selecionado (0 para simulação, 1 para processamento de dados).
        readers (int): Número de clusters principais a serem criados.
        time_readings (int): Tempo de parada para leitura por ponto
        hork_hours (int): Tempo de trabalho máximo diário
        total_days (int): Número total de dias de trabalho

    Returns:
        float: Tempo total em minutos para executar a simulação e o percurso dos pontos.
    """
    # Iniciaçização da contagem de tempo para execução do algoritmo
    global_two_opt = 0
    time_start = time.time()

    # Executa o algoritmo selecionado e retorna o tempo necessário para sua execução
    if select_algo == 0:
        df, total_minutes_clustering = simulate(readers, total_days)
        # Reduz o tamanho do DataFrame para testes rápidos
        df = df.head(40)
    elif select_algo == 1:
        df, total_minutes_clustering = process_data(time_readings, hours_work,total_days)
        # Reduz o tamanho do DataFrame para testes rápidos
        df = df.head(40)
        
    # Certifique-se de que as colunas necessárias estão presentes
    required_columns = ['LATITUDE', 'LONGITUDE', 'rotas', 'dia', 'LOGRADOURO', 'NUMERO']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Colunas faltando no DataFrame: {missing_columns}")
    
    columns = ['LATITUDE', 'LONGITUDE', 'rotas', 'dia', 'LOGRADOURO', 'NUMERO']
    output = []
    summary = []
    print("Processamento começou!!!")

    # Itera por rota e dia, para verificar o tempo e distância para cada uma dessas instâncias
    for (route, day), group in df.groupby(['rotas', 'dia']):
        points = group[['LATITUDE', 'LONGITUDE']].values
        tsp_order = nearest_neighbor(points)
        optimized_tsp_order, local_two_opt = two_opt(tsp_order, points)
        global_two_opt += local_two_opt
        print(global_two_opt)

        total_distance = 0
        total_time = time_readings / 60  # Initial 1 minute stop time
        first_point = optimized_tsp_order[0]
        origem_endereco = f"{group.iloc[first_point]['LOGRADOURO']}, {group.iloc[first_point]['NUMERO']}"
        origem_lat = group.iloc[first_point]['LATITUDE']
        origem_lon = group.iloc[first_point]['LONGITUDE']
        # Formatação para o json de resposta
        output.append({
            'origem': origem_endereco,
            'destino': origem_endereco,
            'origem_latitude': origem_lat,
            'origem_longitude': origem_lon,
            'destino_latitude': origem_lat,
            'destino_longitude': origem_lon,
            'tempo': f"{total_time * 60:.2f} minutos",
            'distancia': f"{0.0}",
            'leiturista': f"{route}",
            'dia': f"{day}"
        })

        # Formatação para o json de resposta
        for i in range(1, len(optimized_tsp_order)):
            previous_point = optimized_tsp_order[i-1]
            current_point = optimized_tsp_order[i]
            distance = haversine_distance(points[previous_point, 0], points[previous_point, 1], points[current_point, 0], points[current_point, 1])
            time_sec = distance / 5 + time_readings / 60  # Speed is 5km/h, 1 minute per stop
            origem_endereco = f"{group.iloc[previous_point]['LOGRADOURO']}, {group.iloc[previous_point]['NUMERO']}"
            destino_endereco = f"{group.iloc[current_point]['LOGRADOURO']}, {group.iloc[current_point]['NUMERO']}"
            origem_lat = group.iloc[previous_point]['LATITUDE']
            origem_lon = group.iloc[previous_point]['LONGITUDE']
            destino_lat = group.iloc[current_point]['LATITUDE']
            destino_lon = group.iloc[current_point]['LONGITUDE']
            output.append({
                'origem': origem_endereco,
                'destino': destino_endereco,
                'origem_latitude': origem_lat,
                'origem_longitude': origem_lon,
                'destino_latitude': destino_lat,
                'destino_longitude': destino_lon,
                'tempo': f"{time_sec * 60:.2f} minutos",
                'distancia': f"{distance} km",
                'leiturista': f"{route}",
                'dia': f"{day}"
            })
            total_distance += distance
            total_time += time_sec

        # Verificar se o tempo na rota diária é abaixo, correto ou excedido
        alert = 0
        total_hours = total_time
        if total_hours < (hours_work + 50/60):
            alert = -1
        elif (hours_work + 50/60) <= total_hours <= (hours_work + 5/60):
            alert = 0
        else:
            alert = 1

        # Formatação para o json de resposta de sumario
        summary.append({
            'rota': f'Rota {route}',
            'dia': f"{day}",
            'tempo': f"{total_time * 60:.2f} minutos",
            'distancia': f"{total_distance:.2f} km",
            'leiturista': f"{route}",
            'alerta': 'Ok' if alert == 0 else ('Insuficiente' if alert == -1 else 'Excedido')
        })

    # Caminho relativo para a pasta output dentro de backend
    folder_path = './output'

    # Cria a pasta se ela não existir
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Caminho completo para os arquivos
    detailed_data_file_path = os.path.join(folder_path, 'detailed_data.json')
    summary_file_path = os.path.join(folder_path, 'summary.json')

    # Escreve os arquivos em json
    with open(detailed_data_file_path, 'w') as file:
        json.dump(output, file, indent=4)

    with open(summary_file_path, 'w') as file:
        json.dump(summary, file, indent=4)

    # Retorna o tempo total para executar o algoritmo (Tempo clusters + tempo percorredor) em minutos
    time_end = time.time()
    total_time = time_end - time_start
    total_minutes_walking = total_time / 60
    total_minutes = total_minutes_walking + total_minutes_clustering
    print(f"Processamento terminou!!! Tempo total: {total_minutes:.2f} minutos")
    return total_minutes
