from pyexpat import model
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

import os

dag_id = "proj"
home_path = os.path.expanduser("~")
runpath = os.path.join(home_path, "airflow/data", dag_id)


def load_data(ti):
    import os

    train = os.path.join(runpath, "mnist")
    test = os.path.join(runpath, "mnist.t")
    model = os.path.join(runpath, "trained.mnist")

    if not os.path.exists(train):
        os.system(
            "curl https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multiclass/mnist.bz2 --output mnist.bz2"
        )
        os.system("bzip2 -d mnist.bz2")

    if not os.path.exists(test):
        os.system(
            "curl https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multiclass/mnist.t.bz2 --output mnist.t.bz2"
        )
        os.system("bzip2 -d mnist.t.bz2")

    ti.xcom_push(key="train_path", value=train)
    ti.xcom_push(key="test_path", value=test)
    ti.xcom_push(key="model_path", value=model)


def train(
    **context,
):
    import os

    ti = context["ti"]

    train = ti.xcom_pull(task_ids="load_data", key="train_path")
    model_path = ti.xcom_pull(task_ids="load_data", key="model_path")

    lr = context["dag_run"].conf["lr"]
    epochs = context["dag_run"].conf["epochs"]
    name = context["dag_run"].conf["name"]

    print(lr)
    print(epochs)

    ti.xcom_push(key="model_name", value=model_final_name)


def validate(**context):
    ti = context["ti"]

    test = ti.xcom_pull(task_ids="load_data", key="test_path")
    model_path = ti.xcom_pull(task_ids="train", key="model_name")
    print(test)
    print(model_path)

with DAG(
    dag_id="project",
    default_args={"owner": "airflow"},
    start_date=datetime(2022, 8, 8),
    schedule_interval=timedelta(minutes=3),
    tags=["mnist_4"],
    catchup=False,
) as dag:

    print(runpath)

    os.makedirs(runpath, exist_ok=True)
    os.chdir(runpath)

    read_file = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
        provide_context=True,
    )

    process_train = PythonOperator(
        task_id="train",
        python_callable=train,
        provide_context=True,
    )

    validate = PythonOperator(
        task_id="validate", p
        ython_callable=validate, 
        provide_context=True
    )


read_file >> process_train >> validate