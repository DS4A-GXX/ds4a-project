import random
import logging
from datetime import datetime, date, timedelta
from flask import request
from flask import json
from app.rest import api
from app.rest import auth
from app.serializers import score_input, score_output
from flask_restplus import Resource

log = logging.getLogger(__name__)

ns = api.namespace("health", description="Health Score")


@ns.route("/score/")
class ScoreObject(Resource):
    @auth.login_required
    @api.expect(score_input)
    def post(self):
        data = request.json
        gender = data.get("gender")
        income = data.get("income")
        members = data.get("members")
        birthdate = data.get("birthdate")

        try:

            birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
            age = (date.today() - birthdate) // timedelta(days=365.2425)

            medical_procedures = ["Fisioterapia", "Psiquiatria", "Oftalmologia"]
            medical_procedures.append("Nutrologia")
            medical_procedures.append("Cardiologia")
            medical_procedures.append("Dermatologia")
            medical_procedures.append("Ortopedia")
            options = random.sample(medical_procedures, 3)

            resp = {
                "option_a": options[0],
                "option_b": options[1],
                "option_c": options[2],
            }
            data.update(resp)
            log.info(data)
            return resp

        except ValueError as ve:
            log.error(ve)
            return json.dumps({"message": "Invalid payload."}), 500
        except Exception as e:
            log.error(e)
            return json.dumps(e), 500
