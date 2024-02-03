from airflow.models import DAG

default_args = {
    "start_date": "2023-01-01",
    # (optional) when to stop running new DAG instances
    "end_date": "2023-01-01",
    # (optional) how many attempts to make
    "max_tries": 3,
    "schedule_interval": "@daily",
}

example_dag = DAG(dag_id="scheduling_fundamentals", default_args=default_args)
