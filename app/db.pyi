from gino_sanic import Gino as SanicGino

from gino_starlette import Gino

db: Gino
sanic_db: SanicGino
