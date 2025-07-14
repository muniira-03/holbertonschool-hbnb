from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from hbnb.app.models.db import db
from hbnb.app.models.place import Place

ns = Namespace("places", description="Place operations")

place_model = ns.model("Place", {
    "name": fields.String(required=True, description="Name of the place"),
    "description": fields.String(required=False, description="Description of the place"),
})

@ns.route("/")
class PlaceList(Resource):
    def get(self):
        """Return list of all places"""
        places = Place.query.all()
        return [place.to_dict() for place in places], 200

    @jwt_required()
    @ns.expect(place_model)
    def post(self):
        """Create a new place (authenticated users only)"""
        data = ns.payload

        if not data or not data.get("name"):
            return {"message": "Place name is required"}, 400

        user_id = get_jwt_identity()
        place = Place(name=data["name"], description=data.get("description", ""), user_id=user_id)
        
        try:
            db.session.add(place)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"message": "Error saving place: " + str(e)}, 500

        return place.to_dict(), 201
