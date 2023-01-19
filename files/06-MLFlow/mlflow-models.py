# MLFlow Models

print("MLFlow Models Tutorial Script")


print("> Build and save model")

# Import the sklearn models from mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor

run_name="models-example-run"
params = {"n_estimators": 4, "random_state": 42}

# Start an MLFlow run, train the RandomForestRegressor example model, and 
# log its parameeters. In the end the model itself is logged and stored in MLFlow
run_name = 'logging model example'
with mlflow.start_run(run_name=run_name) as run:
   rfr = RandomForestRegressor(**params).fit([[0, 1, 0]], [1])
   mlflow.log_params(params)
   mlflow.sklearn.log_model(rfr, artifact_path="sklearn-model")

model_uri = "runs:/{}/sklearn-model".format(run.info.run_id)
model_name = f"{namespace}-RandomForestRegressionModel"
print(f"model_uri: {model_uri}")
print(f"model_name: {model_name}")


## ---------------------
print("> Use model for prediction")

import mlflow.pyfunc

# Load the model and use it for predictions
model = mlflow.pyfunc.load_model(model_uri=model_uri)
data = [[0, 1, 0]]
model_pred = model.predict(data)
print(f"model_pred: {model_pred}")


