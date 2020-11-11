# Benchmarks

## fastapi

```bash
uvicorn asgi_fastapi:app --port 8080 --host 0.0.0.0
wrk --latency -t20 -c50 -d15s http://0.0.0.0:8080/api/users/1/bake
wrk --latency -t20 -c50 -d15s http://0.0.0.0:8080/api/users/1/raw
wrk --latency -t20 -c50 -d15s http://0.0.0.0:8080/api/users/1
```

## sanic

Change `from .common import db` to `from .common import sanic_db as db` in `app/models/abstract.py`

```bash
uvicorn asgi_sanic:app --port 8010 --host 0.0.0.0
wrk --latency -t20 -c50 -d15s http://0.0.0.0:8010/api/users/1/bake
wrk --latency -t20 -c50 -d15s http://0.0.0.0:8010/api/users/1/raw
wrk --latency -t20 -c50 -d15s http://0.0.0.0:8010/api/users/1
```
