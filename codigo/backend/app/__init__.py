from flask import Flask

def create_app():
    """
    Cria e configura uma nova instância do aplicativo Flask.

    Esta função configura a aplicação Flask, registra os blueprints
    e retorna a aplicação configurada.

    Returns:
        Flask: A aplicação Flask configurada.
    """
    app = Flask(__name__)

    from .routes import routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app