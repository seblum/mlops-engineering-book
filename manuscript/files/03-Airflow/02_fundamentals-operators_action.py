from airflow.operators.email_operator import EmailOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.models import DAG
from pendulum import datetime
import time

# ----- Action Operators -----

action_operator_fundamentals = DAG(
    dag_id="action_operator_fundamentals",
    start_date=datetime(2023, 1, 1, tz="Europe/Amsterdam"),
    schedule_interval=None,
)


# BashOperator

bash_task = BashOperator(
    task_id="bash_example",
    bash_command='echo "Example Bash!"',
    dag=action_operator_fundamentals,
)


# PythonOperator


def sleep(length_of_time):
    time.sleep(length_of_time)


sleep_task = PythonOperator(
    task_id="sleep",
    python_callable=sleep,
    op_kwargs={"length_of_time": 5},
    dag=action_operator_fundamentals,
)


# EmailOperator
# This Operator has not been testet by seblum
email_task = EmailOperator(
    task_id="email_sales_report",
    to="sales_manager@example.com",
    subject="automated Sales Report",
    html_content="Attached is the latest sales report",
    files="latest_sales.xlsx",
    dag=action_operator_fundamentals,
)
