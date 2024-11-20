from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/sistema_consultorio'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        from .routes import app_routes
        app.register_blueprint(app_routes)

        db.create_all()  # Criação das tabelas no banco de dados
    return app