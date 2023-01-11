from airflow.models import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.dummy_operator import DummyOperator
from pendulum import datetime


# ----- Sensors -----

sensor_operator_fundamentals = DAG(
    dag_id='sensor_operator_fundamentals',
    start_date=datetime(2023, 1, 1, tz="Europe/Amsterdam"),
    schedule_interval=None
)


start_task = DummyOperator(task_id="start")

file_sensor_task = FileSensor(task_id='file_sense',
                              filepath='salesdata.csv',
                              poke_interval=30,
                              dag=sensor_operator_fundamentals
                              )

stop_task = DummyOperator(task_id="stop")


# the following line denotes a workflow, 
# which will be introduced in the next section
start_task >> file_sensor_task >> stop_task
