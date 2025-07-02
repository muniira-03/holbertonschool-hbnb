from flask import Flask
from flask_jwt_extended import JWTManager
from .config import Config
from hbnb.app.api.v1.users import ns as user_ns
from hbnb.app.models.db import db  
from flask_restx import Api

jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)

    api = Api(app, version="1.0", title="HBnB API")
    api.add_namespace(user_ns, path='/api/v1/users')

    return app
