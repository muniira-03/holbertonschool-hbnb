from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from hbnb.app.models.user import User
from hbnb.app import db
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

@ns.route('/')
class UserRegister(Resource):
    @ns.expect(user_model)
    def post(self):
        data = ns.payload
        email = data.get('email')
        password = data.get('password')

       
        user = User.query.filter_by(email=email).first()
        if user:
            return {"error": "User already exists"}, 400
        
        new_user = User(email=email)
        new_user.set_password(password)  

        db.session.add(new_user)
        db.session.commit()

        return new_user.to_dict(), 201

    def get(self):
        users = User.query.all()
        return [u.to_dict() for u in users]

@ns.route('/login')
class UserLogin(Resource):
    @ns.expect(login_model)
    def post(self):
        data = ns.payload
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            access_token = create_access_token(
                identity=user.id,
                additional_claims={"is_admin": user.is_admin},
                expires_delta=timedelta(hours=1)
            )
            return {"access_token": access_token}, 200
        
        return {"error": "Invalid email or password"}, 401
