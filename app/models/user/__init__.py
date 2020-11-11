from collections import namedtuple

from sqlalchemy import Column
from sqlalchemy import String

from ..abstract import Base
from ..abstract import db

UserResult = namedtuple("User", ["id", "name"])


class User(Base):
    __tablename__ = "user"

    name = Column(String, nullable=False)

    @db.bake
    def getter(cls):
        return cls.query.where(cls.id == db.bindparam("uid"))

    @classmethod
    async def get_bake(cls, uid: int):
        return await cls.getter.one_or_none(uid=uid)

    @classmethod
    async def get_raw(cls, uid: int):
        user_id, name = await db.one_or_none(
            f"select id, name from public.user where id = {uid}",
        )
        return UserResult(user_id, name)
