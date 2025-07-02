from flask_jwt_extended import JWTManager
from flask import Flask
from hbnb.app.config import Config
from hbnb.app.api.v1.users import users as users_blueprint
from hbnb.app.models.db import db

jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(users_blueprint)

    return app
