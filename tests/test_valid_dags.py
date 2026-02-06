from airflow.models import DagBag
from airflow.utils import db
import pytest


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
