from flask import Flask
from flask_restx import Api
from hbnb.app.api.v1 import api_v1

def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    app.register_blueprint(api_v1)
    return app
