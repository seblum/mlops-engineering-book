from airflow.models import DAG
from pendulum import datetime
from airflow.operators.python_operator import PythonOperator


xcom_fundamentals = DAG(
    dag_id='xcom_fundamentals',
    start_date=datetime(2023, 1, 1, tz="Europe/Amsterdam"),
    schedule_interval=None
)


# DAG definition etc.
value_1 = [1, 2, 3]
value_2 = {'a': 'b'}


def push(**kwargs):
    """Pushes an XCom without a specific target"""
    kwargs['ti'].xcom_push(key='value from pusher 1', value=value_1)


def push_by_returning(**kwargs):
    """Pushes an XCom without a specific target, just by returning it"""
    # Airflow does this automatically as auto-push is turned on.
    return value_2


def puller(**kwargs):
    """Pull all previously pushed XComs and check if the pushed values match the pulled values."""
    ti = kwargs['ti']

    # get value_1
    pulled_value_1 = ti.xcom_pull(key=None, task_ids='push')

    # get value_2
    pulled_value_2 = ti.xcom_pull(task_ids='push_by_returning')

    # get both value_1 and value_2 the same time
    pulled_value_1, pulled_value_2 = ti.xcom_pull(
        key=None, task_ids=['push', 'push_by_returning'])

    print(f"pulled_value_1: {pulled_value_1}")
    print(f"pulled_value_2: {pulled_value_2}")


push1 = PythonOperator(
    task_id='push',
    # provide context is for getting the TI (task instance ) parameters
    provide_context=True,
    dag=xcom_fundamentals,
    python_callable=push,
)

push2 = PythonOperator(
    task_id='push_by_returning',
    dag=xcom_fundamentals,
    python_callable=push_by_returning,
    # do_xcom_push=False
)

pull = PythonOperator(
    task_id='puller',
    # provide context is for getting the TI (task instance ) parameters
    provide_context=True,
    dag=xcom_fundamentals,
    python_callable=puller,
)

# push1, push2 are upstream to pull
[push1, push2] >> pull
