from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy_utils.functions import database_exists, create_database

db_name = 'postgresql+psycopg2://postgres:postgres@localhost:5432/susdb'
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456abcdef'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = db_name
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Usuarios

    criar_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = u"Entre com os credenciais para acessar o sistema."
    login_manager.login_message_category = "info"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(cns):
        return Usuarios.query.get(str(cns))

    return app

def criar_db(app):
    if not database_exists(db_name):
        create_database(db_name)
        db.create_all(app=app)
        print('Banco de Dados criado!')