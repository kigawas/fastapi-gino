from fastapi import FastAPI
from fastapi_profiler.profiler_middleware import PyInstrumentProfilerMiddleware

from .api import api_router
from .config import DATABASE_URL
from .config import DB_POOL_MAX_SIZE
from .config import DEBUG


def get_app():
    from .db import db

    app = FastAPI()
    if DEBUG:
        app.add_middleware(PyInstrumentProfilerMiddleware)
    db.init_app(app)

    app.include_router(api_router, prefix="/api")
    return app


def get_sanic_app():
    from sanic import Sanic
    from sanic.response import json
    from .models import User
    from .db import sanic_db

    app = Sanic()
    app.config.DB_DSN = DATABASE_URL
    app.config.DB_POOL_MAX_SIZE = DB_POOL_MAX_SIZE
    sanic_db.init_app(app)

    @app.route("/api/users/<pk:int>/raw/asyncpg")
    async def get_user_raw_asyncpg(request, pk: int):
        uid, name = await sanic_db.one_or_none(
            f"select id, name from public.user where id = {pk}"
        )
        return json(dict(id=uid, name=name))

    @app.route("/api/users/<pk:int>/raw")
    async def get_user_raw_gino(request, pk: int):
        user = await User.get_raw(pk)
        return json(dict(id=user.id, name=user.name))

    @app.route("/api/users/<pk:int>/bake")
    async def get_user_bake(request, pk: int):
        user = await User.get_bake(pk)
        return json(dict(id=user.id, name=user.name))

    @app.route("/api/users/<pk:int>")
    async def get_user(request, pk: int):
        user = await User.get(pk)
        return json(dict(id=user.id, name=user.name))

    return app
