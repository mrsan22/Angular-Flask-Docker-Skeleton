# -*- coding: utf-8 -*-

from sqlalchemy import inspect

from server.main import db
from sqlalchemy.sql import func


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self.as_dict().items()
        })

    # def _as_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # Preferred way
    # https://stackoverflow.com/questions/1958219/convert-sqlalchemy-row-object-to-python-dict
    def as_dict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}


class User(BaseModel, db.Model):
    """Model for users table"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    # using func.now(), so time is calculated by the DB server and not by app server.
    # https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    created_date = db.Column(db.DateTime, nullable=False, default=func.now())

    def __init__(self, username, email, password):
        super().__init__()
        self.username = username
        self.email = email
        self.password = password
