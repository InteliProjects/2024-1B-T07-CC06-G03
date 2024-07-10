import pytest
from io import BytesIO
from app import create_app

@pytest.fixture
def client():
    """
    Fixture para criar um cliente de teste para a aplicação.
    """
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """
    Testa se o endpoint '/' retorna a mensagem de boas-vindas esperada.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'mensagem': 'Bem-vindo à API de otimização de rotas E6eu!'}

def test_upload(client, mocker):
    """
    Testa o endpoint '/upload' para verificar se os arquivos CSV são processados corretamente.
    """
    # Simulação da função upload_file
    mock_upload_file = mocker.patch('app.controllers.file_controller.upload_file')
    mock_upload_file.return_value = {'sucesso': True, 'resultados': 'Arquivo salvo como test.csv'}

    # Conteúdo do arquivo CSV
    csv_content = (
        "INDICE;LATITUDE;LONGITUDE;CODIGO_ROTA;SEQUENCIA;LOGRADOURO;NUMERO\n"
        "1;-23.550520;-46.633308;R1;1;Avenida Paulista;1000\n"
        "2;-23.550520;-46.633308;R1;2;Avenida Paulista;2000\n"
    )

    # Dados do upload (arquivo CSV em memória)
    data = {
        'file': (BytesIO(csv_content.encode('utf-8')), 'test.csv')
    }

    # Enviando o POST request para o endpoint /upload
    response = client.post('/upload', content_type='multipart/form-data', data=data)

    # Verificando a resposta
    assert response.status_code == 200
    assert response.json == {'mensagem': 'Arquivo enviado e processado com sucesso', 'resultados': 'Arquivo salvo como test.csv'}

def test_simulation_status(client, mocker):
    """
    Testa se o endpoint '/simulation_status' retorna o status da simulação corretamente.
    """
    mock_get_simulation_status = mocker.patch('app.algorithms.run_simulation.get_simulation_status')
    mock_get_simulation_status.return_value = {'result': None, 'state': 'idle'}

    response = client.get('/simulation_status')
    assert response.status_code == 200
    assert response.json == {'result': None, 'state': 'idle'}

def test_automation_status(client, mocker):
    """
    Testa se o endpoint '/automation_status' retorna o status da automação corretamente.
    """
    mock_get_automation_status = mocker.patch('app.algorithms.run_automation.get_automation_status')
    mock_get_automation_status.return_value = {'result': None, 'state': 'idle'}

    response = client.get('/automation_status')
    assert response.status_code == 200
    assert response.json == {'result': None, 'state': 'idle'}
