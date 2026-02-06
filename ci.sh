#!/usr/bin/env bash

# Exit on fail
set -e

echo "[INFO] running static analysis"
# Some static analysis tools
uv run black . --quiet
uv run flake8 src/ dags.py

echo "[INFO] running tests"
uv run pytest tests/ --ignore=tests/test_valid_dags.py --quiet

echo "[INFO] validating DAGs"
uv run pytest tests/test_valid_dags.py --disable-warnings --quiet

echo "[INFO] building docker image"
make build
