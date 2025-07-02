from flask import request
from flask_restx import Namespace, Resource, fields
from hbnb.app.models.user import User
from hbnb.app.models.db import db

ns = Namespace('users', description='User operations')

user_model = ns.model('User', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@ns.route('/register')
class RegisterUser(Resource):
    @ns.expect(user_model, validate=True)
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if User.query.filter_by(email=email).first():
            return {"error": "User already exists"}, 400

        user = User(email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return user.to_dict(), 201
