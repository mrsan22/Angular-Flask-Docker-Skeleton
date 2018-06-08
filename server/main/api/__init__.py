# -*- coding: utf-8 -*-
"""app.api

    app blueprints/blueprints application package

"""


from server.main import create_app


def create_app_blueprint(config):
    """
    Return the RMIS application instance.

    :param config (str): the environment for the app (dev, test, prod)
    :return: Flask app for RMIS
    """
    app = create_app(config, __name__, __path__)

    return app
