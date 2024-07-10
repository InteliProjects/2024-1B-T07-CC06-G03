import io
import csv
import requests 

"""
Este módulo facilita a interação com APIs para obter dados em formato JSON e a conversão desses dados para o formato CSV. Ele é usado principalmente para acessar informações de rotas específicas de um servidor Flask local e convertê-las em um formato estruturado e portável, como CSV. Isso permite uma fácil exportação e análise de dados coletados ou gerados pela aplicação.

As funções definidas aqui manipulam requisições HTTP para obter os dados desejados e utilizam o módulo io para criar arquivos CSV em memória, que podem ser salvos ou enviados diretamente para os usuários sem a necessidade de armazenamento intermediário.

Funções incluídas:
- get_json_data: Faz uma requisição HTTP para obter dados JSON de uma rota específica. Suporta o tratamento de erros de requisição, garantindo que apenas respostas bem-sucedidas sejam processadas.
- generate_csv_from_json: Utiliza os dados obtidos pela função get_json_data para gerar um arquivo CSV. Isso é feito em memória usando um buffer de strings, o que evita a necessidade de manipulação de arquivos no sistema de arquivos local.

"""


def get_json_data(route_type):
    """
    Obtém dados JSON de uma rota específica.

    Parâmetros:
    route_type (str): O tipo de rota a ser acessada ('detailed' ou 'summary').

    Retorna:
    dict: Os dados JSON retornados pela rota.

    Lança:
    HTTPError: Se a requisição HTTP falhar.
    """
    base_url = 'http://localhost:5000'
    route = '/detailed-data' if route_type == 'detailed' else '/summary-data'
    response = requests.get(base_url + route)
    response.raise_for_status()
    return response.json()

def generate_csv_from_json(route_type):
    """
    Gera um arquivo CSV a partir dos dados JSON obtidos de uma rota específica.

    Parâmetros:
    route_type (str): O tipo de rota a ser acessada ('detailed' ou 'summary').

    Retorna:
    bytes: O conteúdo do arquivo CSV em bytes.

    Lança:
    HTTPError: Se a requisição HTTP falhar.
    """
    json_data = get_json_data(route_type)
    
    # Cria um buffer de memória para armazenar os dados CSV
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Escreve os cabeçalhos (keys do primeiro dicionário no JSON)
    if json_data:
        headers = json_data[0].keys()
        writer.writerow(headers)
    
        # Escreve os dados
        for entry in json_data:
            writer.writerow(entry.values())
    
    # Obtem o valor do buffer em bytes
    return output.getvalue().encode('utf-8')
