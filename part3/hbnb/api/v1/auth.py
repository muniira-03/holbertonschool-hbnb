from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import create_access_token
from hbnb.models.user import User

ns = Namespace("auth", description="Auth operations")

login_model = ns.model("Login", {
    "email": fields.String(required=True),
    "password": fields.String(required=True)
})

@ns.route("/login")
class Login(Resource):
    @ns.expect(login_model)
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data["email"]).first()
        if not user or not user.check_password(data["password"]):
            return {"message": "Invalid credentials"}, 401

        access_token = create_access_token(identity=user.id, additional_claims={"is_admin": user.is_admin})
        return {"access_token": access_token}, 200
