# agimage

Small Python monorepo for the agimage service.

## Layout

- `services/api`: FastAPI entrypoint
- `services/worker`: background worker entrypoint
- `packages/domain`: shared pure application code
- `packages/infra`: shared infrastructure-facing code

## Development

Install the whole workspace into `.venv`:

```bash
uv sync --all-packages
```

Run the API:

```bash
uv run --package agimage_api uvicorn agimage_api.main:app --reload
```

Run the worker:

```bash
uv run --package agimage_worker python -m agimage_worker.main
```
