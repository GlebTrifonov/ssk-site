FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:0.9.7 /uv /bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev --locked
COPY . .
CMD ["uv", "run", "--no-dev", "python", "manage.py", "runserver", "0.0.0.0:8000" ]