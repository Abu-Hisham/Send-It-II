from flask import Flask, Blueprint
from app.instance.config import app_config
from app.api.V1.routes import bp


def create_app(config_name):
    app = Flask(__name__, instance_path='/app/instance/')
    app.config.from_object(app_config[config_name])
    app.register_blueprint(bp)
    return app
