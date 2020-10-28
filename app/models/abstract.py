from sqlalchemy import Column
from sqlalchemy import Integer

from .common import db


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
