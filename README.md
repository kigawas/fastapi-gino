## fastapi

```bash
uvicorn asgi:app --port 8080 --host 0.0.0.0
wrk --latency -t20 -c500 -d15s http://0.0.0.0:8080/api/users/1/bake
wrk --latency -t20 -c500 -d15s http://0.0.0.0:8080/api/users/1/raw
wrk --latency -t20 -c500 -d15s http://0.0.0.0:8080/api/users/1
```

## sanic

```bash
uvicorn asgi:sanic_app --port 8010 --host 0.0.0.0
wrk --latency -t20 -c500 -d15s http://0.0.0.0:8010/api/users/1/raw
```
