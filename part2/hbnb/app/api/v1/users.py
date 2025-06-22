from flask_restx import Namespace, Resource, fields
from flask import request
from hbnb.app.services.facade import facade

ns = Namespace('users', description='User related operations')

user_model = ns.model('User', {
    'id': fields.String(readonly=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
    'first_name': fields.String(),
    'last_name': fields.String()
})

@ns.route('/')
class UserList(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        users = facade.get_all_users()
        return users

    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        data = request.json
        user = facade.create_user(data)
        return user, 201

@ns.route('/<string:id>')
@ns.param('id', 'The user identifier')
class User(Resource):
    @ns.marshal_with(user_model)
    def get(self, id):
        """Fetch a user given its identifier"""
        user = facade.get_user_by_id(id)
        if not user:
            ns.abort(404, "User not found")
        return user

    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    def put(self, id):
        """Update a user given its identifier"""
        data = request.json
        user = facade.update_user(id, data)
        if not user:
            ns.abort(404, "User not found")
        return user
