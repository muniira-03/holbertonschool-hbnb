from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import create_access_token
from hbnb.app.models.user import User

ns = Namespace('auth', description='Authentication operations')

login_model = ns.model('Login', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

@ns.route('/login')
class Login(Resource):
    @ns.expect(login_model)
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            claims = {"is_admin": user.is_admin}
            access_token = create_access_token(identity=user.id, additional_claims=claims)
            return {'access_token': access_token}, 200
        return {'message': 'Invalid credentials'}, 401

