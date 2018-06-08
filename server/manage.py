"""
Test Suite for Flask. 
To run:
python test_suite test
python test_suite cov
"""

import unittest
from coverage import coverage
from flask_script import Manager

from server.main import db
from server.main.api import create_app_blueprint
from server.main.models.user import User

COV = coverage(
    branch=True,
    include='main/*',
    omit=[
        'tests/*',
        'wsgi.py',
        'settings.py',
        '__init__.py',
        'main/*/__init__.py'
        'main/static/*'
        'main/templates/*'
        'main/import_policy/*'
        'main/models/*'
    ]
)

COV.start()

# create flask application instance
app = create_app_blueprint('development')
manager = Manager(app)


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    test_suite = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report(directory='tests/coverage')
        COV.erase()
        return 0
    return 1

@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@manager.command
def seed_db():
    """Seed the user table in test_db database."""
    db.session.add(User(
        username='sanjiv',
        email='mr.san.kumar@gmail.com',
        password='sanjiv'
    ))
    db.session.add(User(
        username='admin',
        email='admin@gmail.com',
        password='admin'
    ))
    db.session.commit()

if __name__ == '__main__':
    manager.run()
