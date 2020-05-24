# coding=utf-8
import os
from app import settings
import logging
from flask import Flask
from flask import Blueprint
from logging.handlers import RotatingFileHandler
from app.rest import api
from app.endpoint import ns as scorens

log = logging.getLogger()

app = Flask(__name__, instance_relative_config=True)


def setup_log():
    log.setLevel(settings.LOG_LEVEL)
    handler = RotatingFileHandler(
        settings.LOG_FILEPATH,
        maxBytes=settings.LOG_MAX_SIZE,
        backupCount=settings.LOG_HISTORY,
    )
    handler.setLevel(settings.LOG_LEVEL)
    formatter = logging.Formatter(settings.LOG_FORMAT)
    handler.setFormatter(formatter)
    log.addHandler(handler)


def configure_app(flask_app):
    #######################################################################
    # Configura acesso ao db
    #######################################################################
    flask_app.config["RESTPLUS_VALIDATE"] = settings.RESTPLUS_VALIDATE
    flask_app.config["SWAGGER_UI_DOC_EXPANSION"] = settings.SWAGGER_UI_DOC_EXPANSION
    flask_app.config["RESTPLUS_MASK_SWAGGER"] = settings.RESTPLUS_MASK_SWAGGER


def initialize_app(flask_app):
    setup_log()
    configure_app(flask_app)

    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api.init_app(blueprint)
    api.namespaces = []
    api.add_namespace(scorens)
    flask_app.register_blueprint(blueprint)


def get_wsgi_application(wsgi=False):
    initialize_app(app)
    ###########################################################################
    # Incia a aplicação de acordo com os parametros do arquivo de configuração
    # imprime o caminho do arquivo de log para facilitar a operação
    ###########################################################################
    port = settings.HOST_PORT
    debugMode = settings.DEBUG_MODE
    ip_filter = settings.IP_FILTER
    start_msg = "Starting Service at {}:{}/api/ in debugMode:{}"
    start_msg = start_msg.format(ip_filter, port, debugMode)
    print(start_msg)
    logging.info(start_msg)
    if wsgi:
        app.run(port=port, debug=debugMode, host=ip_filter)
    return app


if __name__ == "__main__":
    get_wsgi_application(True)
