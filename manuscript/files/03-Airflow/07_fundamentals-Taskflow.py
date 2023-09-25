import json
import pendulum
from airflow.decorators import dag, task

# Specify the dag using @dag
# The Python function name acts as the DAG identifier
# (see also https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html)


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def taskflow_api_fundamentals():
    # set a task using @task
    @task()
    def extract():
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        order_data_dict = json.loads(data_string)
        return order_data_dict

    @task(multiple_outputs=True)
    def transform(order_data_dict: dict):
        total_order_value = 0
        for value in order_data_dict.values():
            total_order_value += value
        return {"total_order_value": total_order_value}

    @task()
    def load(total_order_value: float):
        print(f"Total order value is: {total_order_value:.2f}")

    # task dependencies are automatically generated
    order_data = extract()
    order_summary = transform(order_data)
    load(order_summary["total_order_value"])


# Finally execute the DAG
taskflow_api_fundamentals()


"""
# Transform method using XComs
def transform(**kwargs):
    ti = kwargs["ti"]
    extract_data_string = ti.xcom_pull(task_ids="extract", key="order_data")
    order_data = json.loads(extract_data_string)

    total_order_value = 0
    for value in order_data.values():
        total_order_value += value

    total_value = {"total_order_value": total_order_value}
    total_value_json_string = json.dumps(total_value)
    ti.xcom_push("total_order_value", total_value_json_string)
"""
