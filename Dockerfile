FROM ghcr.io/astral-sh/uv:debian-slim

COPY . .

RUN uv sync --no-dev

ENTRYPOINT ["uv", "run", "--no-dev", "first"]

CMD ["--help"]
