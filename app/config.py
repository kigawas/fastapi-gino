from pathlib import Path

from starlette.config import Config

p = Path(__file__).parent.parent / ".env"
config = Config(p if p.exists() else None)

DEBUG = config("DEBUG", cast=bool, default=False)
TESTING = config("TESTING", cast=bool, default=False)

DATABASE_URL = config("DATABASE_URL", cast=str, default=None)
if TESTING:
    DATABASE_URL = config("DATABASE_URL_TEST", cast=str, default=None)

DB_POOL_MIN_SIZE = config("DB_POOL_MIN_SIZE", cast=int, default=1)
DB_POOL_MAX_SIZE = config(
    "DB_POOL_MAX_SIZE", cast=int, default=64
)  # bigger size reduces connection acquirement
DB_ECHO = config("DB_ECHO", cast=bool, default=False)
DB_SSL = config("DB_SSL", default=None)
DB_USE_CONNECTION_FOR_REQUEST = config(
    "DB_USE_CONNECTION_FOR_REQUEST", cast=bool, default=False
)  # False reduces connection acquirement
DB_RETRY_LIMIT = config("DB_RETRY_LIMIT", cast=int, default=1)
DB_RETRY_INTERVAL = config("DB_RETRY_INTERVAL", cast=int, default=1)
