from datetime import datetime

from airflow import DAG
from kubernetes.client import models as k8s
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

with DAG(
    dag_id="first_project",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    default_args={
        "owner": "tim",
        "retries": 0,
    },
    tags=["first_project", "team:TIM"],
) as dag:
    run_ml_task = KubernetesPodOperator(
        task_id="first_ingest",
        name="first-ingest",
        image="first_project:dev",
        namespace="airflow-poc",
        arguments=["ingest"],
        get_logs=True,
        is_delete_operator_pod=True,
        container_resources=k8s.V1ResourceRequirements(
            requests={"memory": "1Gi", "cpu": "500m"},
            limits={"memory": "2Gi", "cpu": "1000m"},
        ),
        labels={"project": "first_project", "team": "TIM"},
    )
