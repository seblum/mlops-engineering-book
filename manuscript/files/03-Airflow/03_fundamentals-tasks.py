from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from pendulum import datetime


# ----- Action Operators -----

task_fundamentals = DAG(
    dag_id="task_fundamentals",
    start_date=datetime(2023, 1, 1, tz="Europe/Amsterdam"),
    schedule_interval=None,
)

task_1 = BashOperator(task_id="print_date", bash_command="date", dag=task_fundamentals)

task_2 = BashOperator(
    task_id="set_sleep",
    depends_on_past=False,
    bash_command="sleep 5",
    retries=3,
    dag=task_fundamentals,
)

task_3 = BashOperator(
    task_id="print_success",
    depends_on_past=False,
    bash_command='echo "Success!"',
    dag=task_fundamentals,
)


# Simply chained dependencies
task_1 >> task_2 >> task_3

# -----
# Mixed dependencies
# task_1 >> task_3 << task_2
#
# which is similar to
# task_1 >> task_3
# task_2 >> task_3
#
# or
# [task_1, task_2] >> task_3

# -----
# It is also possible to define dependencies with
# task_1.set_downstream(task_2)
# task_3.set_upstream(task_1)

# -----
# It is also possible to mix it completely wild
# task_1 >> task_3 << task_2
# task_1.set_downstream(task_2)
