# coding=utf-8
import logging
import traceback
from flask_jwt import JWTError
from flask_restplus import Api
from flask_httpauth import HTTPBasicAuth


log = logging.getLogger(__name__)

api = Api(version="1.0", title="Vitalicia Model API", description="Health Score")

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username == "vital" and password == "vital_e_sua_m0t0+queUniaoFeLiZ":
        return True
    else:
        return False


@api.errorhandler
def default_error_handler(e):
    message = str(e)
    log.exception(message)
    return {"message": message}, 500


@api.errorhandler(JWTError)
def authentication_error(e):
    log.warning(traceback.format_exc())
    return {"message": traceback.error_message}, 401
