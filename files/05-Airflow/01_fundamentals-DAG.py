from airflow.models import DAG
from pendulum import datetime

# Using extra arguments allows to customize in a clear structure
# e.g. when setting the time zone in a DAG.
default_args = {
    'start_date': datetime(2023, 1, 1, tz="Europe/Amsterdam"),
    'schedule_interval': 'None'
}

example_dag = DAG(
    dag_id='DAG_fundamentals',
    default_args=default_args
)
