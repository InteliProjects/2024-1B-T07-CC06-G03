from flask_cors import CORS
from app import create_app

app = create_app()
CORS(app, origins='http://localhost:5173')

if __name__ == '__main__':
    """
    Ponto de entrada para iniciar a aplicação Flask.

    Este script cria uma instância da aplicação Flask e a executa em modo de depuração.
    A configuração de CORS permite que o frontend localizado em 'http://localhost:5173' 
    faça requisições à API Flask.

    Notas:
        - O modo de depuração (`debug=True`) é ativado, o que não é recomendado para ambientes de produção.
    """
    app.run(debug=True)
