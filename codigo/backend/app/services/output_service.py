import json
from flask import jsonify

"""
Este módulo é responsável por fornecer acesso a dados de simulação armazenados em formato JSON através de endpoints da API Flask. As funções dentro deste módulo carregam dados de arquivos JSON e os retornam como respostas formatadas em JSON usando o Flask. Isso permite que clientes da API, como interfaces de usuário web ou outros sistemas, acessem os dados de simulação de forma programática e em tempo real.

Os dados são armazenados em dois formatos: detalhado e resumido, correspondendo às funções get_detailed_data e get_summary_data, respectivamente. Esses dados podem ser usados para análises aprofundadas ou para uma visão geral rápida do resultado das simulações, facilitando a tomada de decisões baseadas em dados e a comunicação de informações importantes para os usuários.

Funções incluídas:
- get_detailed_data: Carrega e retorna os dados detalhados de uma simulação a partir de um arquivo JSON. Este dado inclui informações específicas sobre cada etapa ou componente da simulação.
- get_summary_data: Carrega e retorna uma visão resumida dos dados da simulação, focando em pontos-chave e métricas agregadas que fornecem uma visão rápida do desempenho ou resultado da simulação.

"""


def get_detailed_data():
    """
    Retorna os dados detalhados da simulação.

    Returns:
        Response: Objeto de resposta Flask com os dados detalhados em formato JSON.
    """
    with open('./output/detailed_data.json') as file:
        data = json.load(file)
    return jsonify(data)


def get_summary_data():
    """
    Retorna os dados resumidos da simulação.

    Returns:
        Response: Objeto de resposta Flask com os dados resumidos em formato JSON.
    """
    with open('./output/summary.json') as file:
        data = json.load(file)
    return jsonify(data)