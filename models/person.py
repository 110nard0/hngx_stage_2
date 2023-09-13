#!/usr/bin/env python3
""" Person module
"""
from dataclasses import dataclass
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import db


@dataclass
class Person(db.Model):
    """ Person class
    """
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
