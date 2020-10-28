from collections import namedtuple

from sqlalchemy import Column
from sqlalchemy import String

from ..abstract import Base
from ..abstract import db


class User(Base):
    __tablename__ = "user"

    name = Column(String, nullable=False)

    @db.bake
    def getter(cls):
        return cls.query.where(cls.id == db.bindparam("uid"))

    @classmethod
    async def get_bake(cls, uid):
        return await cls.getter.one_or_none(uid=uid)

    @classmethod
    async def get_raw(cls, uid):
        user_id, name = await db.one_or_none(
            f"select id, name from public.user where id = {uid}",
        )
        return namedtuple("User", ["id", "name"])(user_id, name)
