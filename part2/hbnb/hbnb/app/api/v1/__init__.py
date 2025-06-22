from flask import Blueprint

api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')

from .users import ns as users_ns
from .amenities import ns as amenities_ns
from .places import ns as places_ns
from .reviews import ns as reviews_ns

from flask_restx import Api

api = Api(api_v1_bp,
          title='HBnB API',
          version='1.0',
          description='HBnB API V1')

api.add_namespace(users_ns)
api.add_namespace(amenities_ns)
api.add_namespace(places_ns)
api.add_namespace(reviews_ns)
