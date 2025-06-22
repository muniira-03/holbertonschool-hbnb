from flask_restx import Namespace, Resource

ns = Namespace('reviews', description='Reviews operations')

@ns.route('/')
class ReviewsList(Resource):
    def get(self):
        return {"message": "List of reviews"}

    def post(self):
        return {"message": "Create a new review"}, 201

@ns.route('/<string:id>')
class Review(Resource):
    def get(self, id):
        return {"message": f"Get review with id {id}"}

    def put(self, id):
        return {"message": f"Update review with id {id}"}

    def delete(self, id):
        return {"message": f"Delete review with id {id}"}

