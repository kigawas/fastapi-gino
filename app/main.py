from fastapi import FastAPI

from .api import api_router
from .config import DATABASE_URL
from .config import DB_POOL_MAX_SIZE
from .db import db
from .db import sanic_db


def get_app():
    app = FastAPI()
    db.init_app(app)

    app.include_router(api_router, prefix="/api")
    return app


def get_sanic_app():
    from sanic import Sanic
    from sanic.response import json

    app = Sanic()
    app.config.DB_DSN = DATABASE_URL
    app.config.DB_POOL_MAX_SIZE = DB_POOL_MAX_SIZE
    sanic_db.init_app(app)

    @app.route("/api/users/<pk>/raw")
    async def get_user(request, pk: int):
        uid, name = await sanic_db.one_or_none(
            f"select id, name from public.user where id = {pk}"
        )
        return json(dict(id=uid, name=name))

    return app
