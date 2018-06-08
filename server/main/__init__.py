# -*- coding: utf-8 -*-
"""Angular-Flask-Docker-Skeleton

    Main application package

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from server.main.utils.common import register_blueprints
from server.settings import config

# instantiate the db
db = SQLAlchemy()

def create_app(config_type, package_name, package_path):
    app = Flask(__name__, instance_relative_config=True)
    # set default config
    # app_settings = os.getenv('APP_DEV_SETTINGS')
    app_settings = config[config_type]
    app.config.from_object(app_settings)

    # instantiate the db
    db.init_app(app)

    # Access config variables as: app.config['DEBUG']
    # Register all api blueprints found in the application
    register_blueprints(app, package_name, package_path)

    return app
