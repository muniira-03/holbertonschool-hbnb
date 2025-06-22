from flask import Blueprint
from flask_restx import Api

from .users import ns as users_ns
from .amenities import ns as amenities_ns
from .places import ns as places_ns
from .reviews import ns as reviews_ns

api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(api_v1_bp, version='1.0', title='HBnB API', description='HBnB RESTful API')

api.add_namespace(users_ns)
api.add_namespace(amenities_ns)
api.add_namespace(places_ns)
api.add_namespace(reviews_ns)
