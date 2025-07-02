from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restx import Api
from hbnb.app.config import Config
from hbnb.app.models.db import db
from hbnb.app.api.v1.users import ns as users_namespace

jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)

    api = Api(app, version='1.0', title='HBnB API')
    api.add_namespace(users_namespace, path='/api/v1/users')

    return app
