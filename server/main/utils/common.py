# -*- coding: utf-8 -*-

import pkgutil
import importlib

from flask import Blueprint


def register_blueprints(app, package_name, package_path):
    """Register all Blueprint instances on the specified Flask application found in all modules
    for the specified package.

    :param app (Flask): the Flask application
    :param package_name (str): the package name
    :param package_path (list): the package path
    :return rv (list): list of blueprints
    """
    blue_prints = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        files = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(files):
            item = getattr(files, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            blue_prints.append(item)
    return blue_prints