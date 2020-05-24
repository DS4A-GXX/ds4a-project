from flask_restplus import fields
from app.rest import api

score_input = api.model(
    "Score Request",
    {
        "gender": fields.String(required=True, description="Person gender"),
        "income": fields.String(required=True, description="Annual family Income"),
        "members": fields.Integer(required=True, description="Family members"),
        "birthdate": fields.String(required=True, description="Person birthdate"),
    },
)


score_output = api.model(
    "Score Response",
    {
        "option_a": fields.String(required=True, description="Option A"),
        "option_b": fields.String(required=True, description="Option B"),
        "option_c": fields.String(required=True, description="Option C"),
    },
)
