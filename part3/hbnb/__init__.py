from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restx import Api
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    
    db.init_app(app)
    jwt.init_app(app)

    
    from .api.v1 import api_v1
    api = Api(app, version="1.0", title="HBnB API")
    api.add_namespace(api_v1)

    with app.app_context():
        db.create_all()  

    return app
