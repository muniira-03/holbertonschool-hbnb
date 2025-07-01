from flask import Flask
from hbnb.api.v1.auth import ns as auth_ns
from flask_restx import Api

def create_app(config_class=None):
    app = Flask(__name__)
    if config_class:
        app.config.from_object(config_class)

    api = Api(app, version='1.0', title='HBnB API', description='HBnB Clone API')

    api.add_namespace(auth_ns, path='/api/v1/auth')

    return app
