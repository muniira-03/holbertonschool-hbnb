from flask import Blueprint
from flask_restx import Api

from .auth import ns as auth_ns
from .places import ns as places_ns

api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(api_v1_bp, version='1.0', title='HBnB API', description='HBnB Clone API')

api.add_namespace(auth_ns)
api.add_namespace(places_ns)
