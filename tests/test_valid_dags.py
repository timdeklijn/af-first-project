"""
This test module validates that Airflow can successfully discover and
parse our DAGs before they are deployed.

Why this validation matters
---------------------------
Airflow loads DAGs by importing Python modules from the `dag_folder`.
If any of those modules has import-time errors (syntax issues, missing
dependencies, bad references, etc.), Airflow will:

* fail to load the affected DAG, and
* record the problem in `DagBag.import_errors`.

Those failures can be easy to miss if we only discover them in a live
scheduler / webserver environment. By running these tests in CI, we
get fast feedback that:

* all DAG files are syntactically valid and importable, and
* core/expected DAGs (such as `first_project`) are present and can be
  constructed into `DAG` objects.

How we validate
---------------
* `dag_bag` is created with `DagBag(dag_folder=".", include_examples=False)`,
  which scans the current directory for DAG definitions, mimicking what
  Airflow does in production.
* `test_import_errors` asserts that `dag_bag.import_errors` is empty,
  meaning every discovered DAG file imported cleanly.
* `test_first_project_dag_is_loaded` asserts that a specific, critical
  DAG (`dag_id="first_project"`) is present and loadable.

Together these tests act as a lightweight "health check" on our DAG
codebase, catching breaking changes early and ensuring that the scheduler
will be able to load and run our workflows once deployed.
"""

import pytest
from airflow.models import DagBag
from airflow.utils import db


@pytest.fixture(scope="session", autouse=True)
def init_db():
    db.initdb()


@pytest.fixture
def dag_bag():
    return DagBag(dag_folder=".", include_examples=False)


def test_import_errors(dag_bag):
    assert len(dag_bag.import_errors) == 0


def test_first_project_dag_is_loaded(dag_bag):
    d = dag_bag.get_dag(dag_id="first_project")
    assert d is not None
