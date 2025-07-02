from flask import Flask
from flask_jwt_extended import JWTManager
from .config import Config
from hbnb.app.api.v1 import api_v1
from hbnb.app.models.db import db  

jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)  
    jwt.init_app(app)

    app.register_blueprint(api_v1)

    return app
