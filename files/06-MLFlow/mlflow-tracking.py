# MLFlow Tracking

from sklearn.ensemble import RandomForestRegressor
import numpy as np
import mlflow.sklearn
import os
from mlflow.tracking import MlflowClient
import mlflow
print("MLFlow Model Tracking Script")


# ---------------------
# MLFlow experiment
print("> MLFlow experiment")


experiment_name = "introduction-experiment"
mlflow.set_experiment(experiment_name)


# ---------------------
# MLFlow run
print("> MLFlow run")


run_name = "example-run"

mlflow.start_run()
run = mlflow.active_run()
print(f"Active run_id: {run.info.run_id}")
mlflow.end_run()


run_name = "context-manager-run"

with mlflow.start_run(run_name=run_name) as run:
    run_id = run.info.run_id
    print(f"Active run_id: {run_id}")


# ---------------------
# Child runs
print("> Child runs")

# Create child runs based on the run ID
with mlflow.start_run(run_id=run_id) as parent_run:
    print("parent run_id: {}".format(parent_run.info.run_id))
    with mlflow.start_run(nested=True, run_name="test_dataset_abc.csv") as child_run:
        mlflow.log_metric("acc", 0.91)
        print("child run_id : {}".format(child_run.info.run_id))

with mlflow.start_run(run_id=run_id) as parent_run:
    print("parent run_id: {}".format(parent_run.info.run_id))
    with mlflow.start_run(nested=True, run_name="test_dataset_xyz.csv") as child_run:
        mlflow.log_metric("acc", 0.90)
        print("child run_id : {}".format(child_run.info.run_id))


# ---------------------
# Logging metrics & parameters
print("> Logging metrics & parameters")

run_name = "tracking-example-run"
experiment_name = "tracking-experiment"
mlflow.set_experiment(experiment_name)

with mlflow.start_run(run_name=run_name) as run:

    # Parameters
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_params({"epochs": 0.05, "final_activation": "sigmoid"})

    # Tags
    mlflow.set_tag("env", "dev")
    mlflow.set_tags({"some_tag": False, "project": "xyz"})

    # Metrics
    mlflow.log_metric("loss", 0.001)
    mlflow.log_metrics({"acc": 0.92, "auc": 0.90})

    # It is possible to log a metrics series (for example a training history)
    for val_loss in [0.1, 0.01, 0.001, 0.00001]:
        mlflow.log_metric("val_loss", val_loss)

    for val_acc in [0.6, 0.6, 0.8, 0.9]:
        mlflow.log_metric("val_acc", val_acc)

    run_id = run.info.run_id
    experiment_id = run.info.experiment_id
    print(f"run_id: {run_id}")
    print(f"experiment_id: {experiment_id}")


# add a note to the experiment
MlflowClient().set_experiment_tag(
    experiment_id, "mlflow.note.content", "my experiment note")
# add a note to the run
MlflowClient().set_tag(run_id, "mlflow.note.content", "my run note")

# Or we can even log further metrics by calling mlflow.start_run on a specific ID
with mlflow.start_run(run_id=run_id):
    run = mlflow.active_run()
    mlflow.log_metric("f1", 0.9)
    print(f"run_id: {run.info.run_id}")


# ---------------------
# Display & View metrics
print("> Display & View metrics")

current_experiment = dict(mlflow.get_experiment_by_name(experiment_name))
mlflow_run = mlflow.search_runs([current_experiment['experiment_id']])
print(f"mlflow_run: {mlflow_run}")


# ---------------------
# Logging artifacts
print("> Logging artifacts")


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
mlflow.set_tracking_uri("http://127.0.0.1:5005/")
=======
mlflow.set_tracking_uri("http://127.0.0.1:5004/")
>>>>>>> 2ca0f2d (code test und initial images)
=======
mlflow.set_tracking_uri("http://127.0.0.1:5000/")
>>>>>>> cd2e73c (added final code)
=======
mlflow.set_tracking_uri("http://127.0.0.1:5005/")
>>>>>>> f9dbc0f (added clipicture)

# Create an example file output/test.txt
file_path = "outputs/test.txt"
if not os.path.exists("outputs"):
    os.makedirs("outputs")
with open(file_path, "w") as f:
    f.write("hello world!")

# Start the run based on the run ID and log the artifact
# we just created
with mlflow.start_run(run_id=run_id) as run:
    mlflow.log_artifact(
        local_path=file_path,
        # store the artifact directly in run's root
        artifact_path=None
    )
    mlflow.log_artifact(
        local_path=file_path,
        # store the artifact in a specific directory
        artifact_path="data/subfolder"
    )

    # get and print the URI where the artifacts have been logged to
    artifact_uri = mlflow.get_artifact_uri()
    print(f"run_id: {run.info.run_id}")
    print(f"Artifact uri: {artifact_uri}")


# ---------------------
# Autolog
print("> Autolog")


params = {"n_estimators": 4, "random_state": 42}

mlflow.sklearn.autolog()

run_name = 'autologging model example'
with mlflow.start_run(run_name=run_name) as run:
    rfr = RandomForestRegressor(
        **params).fit(np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), [1, 1, 1])
    print(f"run_id: {run.info.run_id}")

mlflow.sklearn.autolog(disable=True)
