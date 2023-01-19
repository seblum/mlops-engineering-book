# MLFlow Models

import mlflow.pyfunc
from sklearn.ensemble import RandomForestRegressor
import mlflow.sklearn
import mlflow
print("MLFlow Models Tutorial Script")


experiment_name = "models-experiment"
mlflow.set_experiment(experiment_name)


print("> Build and save model")

# Import the sklearn models from mlflow

<<<<<<< HEAD
mlflow.set_tracking_uri("http://127.0.0.1:5000/")
=======
mlflow.set_tracking_uri("http://127.0.0.1:5004/")
>>>>>>> 2ca0f2d (code test und initial images)

run_name = "models-example-run"
params = {"n_estimators": 4, "random_state": 42}

# Start an MLFlow run, train the RandomForestRegressor example model, and
# log its parameeters. In the end the model itself is logged and stored in MLFlow
run_name = 'Model example'
with mlflow.start_run(run_name=run_name) as run:
    rfr = RandomForestRegressor(**params).fit([[0, 1, 0]], [1])
    mlflow.log_params(params)
    mlflow.sklearn.log_model(rfr, artifact_path="sklearn-model")

model_uri = "runs:/{}/sklearn-model".format(run.info.run_id)
model_name = f"RandomForestRegressionModel"

print(f"model_uri: {model_uri}")
print(f"model_name: {model_name}")


# ---------------------
print("> Use model for prediction")


# Load the model and use it for predictions
model = mlflow.pyfunc.load_model(model_uri=model_uri)
data = [[0, 1, 0]]
model_pred = model.predict(data)
print(f"model_pred: {model_pred}")
