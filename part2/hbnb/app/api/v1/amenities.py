from flask_restx import Namespace, Resource

ns = Namespace('amenities', description='Amenities operations')

@ns.route('/')
class AmenitiesList(Resource):
    def get(self):
        return {"message": "List of amenities"}

    def post(self):
        return {"message": "Create a new amenity"}, 201

@ns.route('/<string:id>')
class Amenity(Resource):
    def get(self, id):
        return {"message": f"Get amenity with id {id}"}

    def put(self, id):
        return {"message": f"Update amenity with id {id}"}
