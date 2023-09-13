#!/usr/bin/env python3
""" Base module
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """ Base class
    """
    @staticmethod
    def validate_id(uid: int) -> bool:
        """ Verify object ID is a valid integer
        Args:
            uid (int): Unique auto-generated database ID
        Return:
            True (bool): uid is a valid, positive integer
            False (bool): uid is not a valid, non-negative integer
        """
        try:
            uid = int(uid)
            if uid > 0 and isinstance(uid, int):
                return True
            return False
        except Exception:
            return False

    @staticmethod
    def validate_name(name: str) -> bool:
        """ Verify object name is a valid string
        Args:
            name (str): Value of object name attribute
        Return:
            True (bool): name is a valid string
            False (bool): name is not a valid string
        """
        return True if name and type(name) is str else False


db = SQLAlchemy(model_class=Base)
