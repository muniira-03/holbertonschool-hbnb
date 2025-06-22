from flask_restx import Namespace, Resource

ns = Namespace('places', description='Places operations')

@ns.route('/')
class PlacesList(Resource):
    def get(self):
        return {"message": "List of places"}

    def post(self):
        return {"message": "Create a new place"}, 201

@ns.route('/<string:id>')
class Place(Resource):
    def get(self, id):
        return {"message": f"Get place with id {id}"}

    def put(self, id):
        return {"message": f"Update place with id {id}"}
