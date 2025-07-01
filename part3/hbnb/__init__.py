from flask import Flask
from hbnb.api.v1 import api_v1_bp
from hbnb.config import Config
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt = JWTManager(app)

    app.register_blueprint(api_v1_bp)

    return app
