import io
from flask import Blueprint, jsonify, send_file, request
from app.controllers.file_controller import upload_file
from app.services.donwload_service import generate_csv_from_json
from app.services.filters_service import filter_data_by_date_and_reader
from app.services.output_service import get_detailed_data, get_summary_data
from app.algorithms.run_simulation import start_simulation, get_simulation_status, reset_simulation
from app.algorithms.run_automation import start_automation, get_automation_status, reset_automation

"""
Este módulo define uma série de rotas Flask para uma API de otimização de rotas. As rotas permitem interações diversas, como o upload e download de arquivos, iniciação e monitoramento de simulações e automações, e acesso a dados filtrados ou detalhados das operações. O módulo utiliza uma série de serviços internos para executar tarefas específicas, como manipulação de arquivos, simulação de processos e fornecimento de dados, integrando funcionalidades de diferentes partes do sistema.

O Blueprint 'routes' é utilizado para organizar e registrar as rotas, facilitando a manutenção e expansão da API. Cada rota é projetada para responder a uma necessidade específica da aplicação, desde a gestão de arquivos até a execução e controle de operações complexas como simulações de roteamento.

Rotas Definidas:
- '/': Retorna uma mensagem de boas-vindas.
- '/upload': Permite o upload de arquivos, que são validados e processados.
- '/start_simulation' e '/reset_simulation': Controlam a execução de simulações.
- '/start_automation' e '/reset_automation': Gerenciam a automação de processos.
- '/[detailed|summary]-data': Fornecem acesso a dados operacionais detalhados ou resumidos.
- '/download/[detailed|summary]-data': Permitem o download de dados em formato CSV.
- '/routes/filter/<day>/<reader>': Filtra dados operacionais por dia e por operador.

"""


routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/')
def index():
    """
    Rota raiz que retorna uma mensagem de boas-vindas.

    Returns:
        response (Response): Resposta JSON contendo uma mensagem de boas-vindas.
    """
    return jsonify({'mensagem': 'Bem-vindo à API de otimização de rotas E6eu!'}), 200

@routes_blueprint.route('/upload', methods=['POST'])
def upload():
    """
    Rota para upload de arquivos CSV. O arquivo é processado e validado.

    Returns:
        response (Response): Resposta JSON indicando sucesso ou falha no upload do arquivo.
    """
    if request.method == 'POST':
        result = upload_file()
        if result['sucesso']:
            return jsonify({'mensagem': 'Arquivo enviado e processado com sucesso', 'resultados': result['resultados']}), 200
        else:
            return jsonify({'mensagem': 'Falha no upload do arquivo', 'erro': result['erro']}), 400

@routes_blueprint.route('/start_simulation', methods=['POST'])
def start():
    """
    Rota para iniciar a simulação de rotas.

    Returns:
        response (Response): Resposta JSON indicando o status da simulação.
    """
    return start_simulation(request)

@routes_blueprint.route('/simulation_status', methods=['GET'])
def status():
    """
    Rota para obter o status atual da simulação.

    Returns:
        response (Response): Resposta JSON contendo o status da simulação.
    """
    return get_simulation_status()

@routes_blueprint.route('/reset_simulation', methods=['GET'])
def reset():
    """
    Rota para resetar o status da simulação.

    Returns:
        response (Response): Resposta JSON indicando que a simulação foi resetada.
    """
    return reset_simulation()

@routes_blueprint.route('/start_automation', methods=['POST'])
def start_automation_route():
    """
    Rota para iniciar a automação de rotas.

    Returns:
        response (Response): Resposta JSON indicando o status da automação.
    """
    return start_automation(request)

@routes_blueprint.route('/automation_status', methods=['GET'])
def automation_status():
    """
    Rota para obter o status atual da automação.

    Returns:
        response (Response): Resposta JSON contendo o status da automação.
    """
    return get_automation_status()

@routes_blueprint.route('/reset_automation', methods=['GET'])
def reset_automation_route():
    """
    Rota para resetar o status da automação.

    Returns:
        response (Response): Resposta JSON indicando que a automação foi resetada.
    """
    return reset_automation()

@routes_blueprint.route('/routes/filter/<int:day>/<int:reader>', methods=['GET'])
def get_filtered_routes(day, reader):
    """
    Rota para filtrar dados por data e leiturista.

    Args:
        dia (int): O dia para filtrar os dados.
        leiturista (int): O ID do leiturista para filtrar os dados.

    Returns:
        response (Response): Dados filtrados em formato JSON.
    """
    filtered_data = filter_data_by_date_and_reader(day, reader)
    return jsonify(filtered_data)

@routes_blueprint.route('/detailed-data', methods=['GET'])
def detailed_data_route():
    """
    Rota para obter os dados detalhados.

    Returns:
        response (Response): Dados detalhados em formato JSON.
    """
    return get_detailed_data()

@routes_blueprint.route('/summary-data', methods=['GET'])
def summary_data_route():
    """
    Rota para obter os dados sumarizados.

    Returns:
        response (Response): Dados sumarizados em formato JSON.
    """
    return get_summary_data()

@routes_blueprint.route('/download/detailed-data', methods=['GET'])
def download_detailed_data():
    """
    Rota para download dos dados detalhados em formato CSV.

    Retorna:
    Response: Um arquivo CSV contendo os dados detalhados, configurado para download.
    """
    csv_file = generate_csv_from_json('detailed')
    return send_file(
        io.BytesIO(csv_file),
        mimetype='text/csv',
        as_attachment=True,
        download_name='detailed_data.csv'
    )

@routes_blueprint.route('/download/summary-data', methods=['GET'])
def download_summary_data():
    """
    Rota para download dos dados resumidos em formato CSV.

    Retorna:
    Response: Um arquivo CSV contendo os dados resumidos, configurado para download.
    """
    csv_file = generate_csv_from_json('summary')
    return send_file(
        io.BytesIO(csv_file),
        mimetype='text/csv',
        as_attachment=True,
        download_name='summary_data.csv'
    )