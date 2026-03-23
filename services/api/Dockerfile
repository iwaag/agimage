FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml README.md uv.lock* /app/
COPY services/api/pyproject.toml services/api/README.md /app/services/api/
COPY services/worker/pyproject.toml services/worker/README.md /app/services/worker/
COPY packages/domain/pyproject.toml /app/packages/domain/
COPY packages/infra/pyproject.toml /app/packages/infra/

RUN uv sync --frozen --all-packages

COPY services/api/src /app/services/api/src
COPY services/worker/src /app/services/worker/src
COPY packages/domain/src /app/packages/domain/src
COPY packages/infra/src /app/packages/infra/src
COPY services/api/entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

CMD ["/app/entrypoint.sh"]
