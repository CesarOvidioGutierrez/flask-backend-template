from flask_restx import fields

from app.config.extensions import api 


auth_input_model = api.model("AuthInput", {
    "email": fields.String(description="Email", required=True, example="user@google.com"),
    "password": fields.String(description="Password", required=True, example="password123"),
})

auth_response_model = api.model("AuthResponse", {
    "email": fields.String(description="User's email"),
    "firstName": fields.String(description="User's first name"),
    "lastName": fields.String(description="User's last name"),
    "token": fields.String(description="Authentication token"),
})