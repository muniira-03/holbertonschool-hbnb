from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import create_access_token
from hbnb.app.models.user import User
from datetime import timedelta

ns = Namespace('users', description='Users operations')

user_model = ns.model('User', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

login_model = ns.model('Login', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

users = []

@ns.route('/')
class UserRegister(Resource):
    @ns.expect(user_model)
    def post(self):

        data = ns.payload
        email = data.get('email')
        password = data.get('password')
        # تحقق إذا الإيميل موجود
        for u in users:
            if u.email == email:
                return {"error": "User already exists"}, 400
        user = User(email=email, password=password)
        users.append(user)
        return user.to_dict(), 201

    def get(self):
        
        return [u.to_dict() for u in users]


@ns.route('/login')
class UserLogin(Resource):
    @ns.expect(login_model)
    def post(self):
        
        data = ns.payload
        email = data.get('email')
        password = data.get('password')

        user = next((u for u in users if u.email == email), None)
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id, additional_claims={"is_admin": user.is_admin}, expires_delta=timedelta(hours=1))
            return {"access_token": access_token}, 200
        return {"error": "Invalid email or password"}, 401
