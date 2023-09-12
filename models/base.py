#!/usr/bin/env python3
""" Base module
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """ Base class
    """
    pass


db = SQLAlchemy(model_class=Base)
