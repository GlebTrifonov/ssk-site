FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:0.9.7 /uv /bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev --locked
COPY . .
CMD ["sh", "-c","uv run --no-dev python manage.py collectstatic --noinput && exec uv run --no-dev gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 30"]
