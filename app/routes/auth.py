from flask import Blueprint
from flask_restx import Api, Resource, Namespace
from http import HTTPStatus

from app.auth import handle_authentication
from app.models import auth_input_model, auth_response_model

AUTH = 'auth'
auth_blueprint = Blueprint(AUTH, __name__)
api = Api(auth_blueprint)
ns_auth = Namespace('api')

@ns_auth.route(f'/{AUTH}')
class Auth(Resource):

    @api.expect(auth_input_model, validate=True)
    @api.response(HTTPStatus.OK, 'Success', auth_response_model)
    def post(self):
        return handle_authentication()

api.add_resource(Auth, f'/{AUTH}')
