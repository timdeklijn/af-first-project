#!/usr/bin/env bash
#
# This file is used to illustrate the steps required in the CI/CD pipeline.

# Exit on fail (just like normal CI)
set -e

# Some static analysis tools, in practice this will contain way more tools, this
# is just to illustrate the sequence in which we do the CI.
echo "[INFO] running static analysis"
uv run black . --quiet
uv run flake8 src/ dags.py

echo "[INFO] running tests"
# Run all tests to validate the logic in the project. Exclude the DAG-validation
# tests.
uv run pytest tests/ --ignore=tests/test_valid_dags.py --quiet

echo "[INFO] validating DAGs"
# Run tests specific for validating the DAGs.
uv run pytest tests/test_valid_dags.py --disable-warnings --quiet

echo "[INFO] building docker image"
# Build the docker container used to run the DAGs in.
make build
