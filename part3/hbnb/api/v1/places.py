from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from hbnb.app.db import db
from hbnb.app.models.place import Place

ns = Namespace("places", description="Place operations")

place_model = ns.model("Place", {
    "name": fields.String(required=True),
    "description": fields.String(required=False),
})

@ns.route("/")
class PlaceList(Resource):
    @jwt_required()
    @ns.expect(place_model)
    def post(self):
        """Create a new place (authenticated users only)"""
        data = ns.payload
        user_id = get_jwt_identity()

        place = Place(name=data["name"], description=data.get("description", ""), user_id=user_id)
        db.session.add(place)
        db.session.commit()

        return place.to_dict(), 201
