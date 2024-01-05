from flask import Blueprint
from flask_restful import Resource, Api

from app.auth.auth import handle_authentication

auth_blueprint = Blueprint('auth', __name__)
api = Api(auth_blueprint)

class Auth(Resource):
    def post(self):
        return handle_authentication()

api.add_resource(Auth, '/auth')
