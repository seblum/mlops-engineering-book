import json
import pendulum
from airflow.decorators import dag, task
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import os
from copy import deepcopy


@dag(
    dag_id="tutorial_mnist_keras_taskflow_api",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example", "mnist", "keras"],
)
def tutorial_mnist_keras_taskflow_api():
    """
    This Airflow DAG demonstrates a simple task flow for training and testing a Keras model on the MNIST dataset.
    It consists of three tasks: preprocess_data, train_model, and test_model.
    """

    @task()
    def preprocess_data():
        """
        Preprocesses the MNIST dataset, scaling it and saving the preprocessed data as NumPy arrays.

        Returns:
            dict: A dictionary containing file paths to the preprocessed data arrays.
        """
        dirname = f"{os.path.dirname(__file__)}/data/"
        print("dirname: ", dirname)

        num_classes = 10
        path = f"{dirname}mnist.npz"

        (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data(path=path)

        # Scale images to the [0, 1] range
        x_train = x_train.astype("float32") / 255
        x_test = x_test.astype("float32") / 255
        # Make sure images have shape (28, 28, 1)
        x_train = np.expand_dims(x_train, -1)
        x_test = np.expand_dims(x_test, -1)
        print("x_train shape:", x_train.shape)
        print(x_train.shape[0], "train samples")
        print(x_test.shape[0], "test samples")

        # convert class vectors to binary class matrices
        y_train = keras.utils.to_categorical(y_train, num_classes)
        y_test = keras.utils.to_categorical(y_test, num_classes)

        y_train_path = f"{dirname}y_train.npy"
        x_train_path = f"{dirname}x_train.npy"
        y_test_path = f"{dirname}y_test.npy"
        x_test_path = f"{dirname}x_test.npy"

        np.save(y_train_path, y_train)
        np.save(x_train_path, x_train)
        np.save(y_test_path, y_test)
        np.save(x_test_path, x_test)

        data_paths_dict = {
            "y_train_path": y_train_path,
            "x_train_path": x_train_path,
            "y_test_path": y_test_path,
            "x_test_path": x_test_path,
        }
        return data_paths_dict

    @task(multiple_outputs=True)
    def train_model(data_paths_dict: dict):
        """
        Trains a Keras model on the preprocessed MNIST dataset.

        Args:
            data_paths_dict (dict): A dictionary containing file paths to the preprocessed data arrays.

        Returns:
            model_data_paths_dict: A dictionary containing file paths to the preprocessed data arrays and the model name after training.
        """
        dirname = f"{os.path.dirname(__file__)}/data/"
        print("dirname: ", dirname)

        ## Load preprocessed train data
        y_train = np.load(data_paths_dict.get("y_train_path"))
        x_train = np.load(data_paths_dict.get("x_train_path"))

        ## Build the model
        input_shape = (28, 28, 1)
        num_classes = 10
        model = keras.Sequential(
            [
                keras.Input(shape=input_shape),
                layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
                layers.MaxPooling2D(pool_size=(2, 2)),
                layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
                layers.MaxPooling2D(pool_size=(2, 2)),
                layers.Flatten(),
                layers.Dropout(0.5),
                layers.Dense(num_classes, activation="softmax"),
            ]
        )
        model.summary()

        ## Train the model
        batch_size = 128
        epochs = 15

        model.compile(
            loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
        )

        model.fit(
            x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1
        )
        model_path = f"{dirname}model.keras"
        model.save(model_path)

        model_data_paths_dict = deepcopy(data_paths_dict)
        model_data_paths_dict["model_name"] = model_path
        return model_data_paths_dict

    @task()
    def test_model(model_data_paths_dict: str):
        """
        Tests a trained Keras model on the test dataset and prints the test loss and accuracy.

        Args:
            model_data_paths_dict: A dictionary containing file paths to the preprocessed data arrays and the model name after training.
        """
        ## Load preprocessed test data
        y_test = np.load(model_data_paths_dict.get("y_test_path"))
        x_test = np.load(model_data_paths_dict.get("x_test_path"))

        model = keras.models.load_model(model_data_paths_dict.get("model_name"))

        score = model.evaluate(x_test, y_test, verbose=0)
        print("Test loss:", score[0])
        print("Test accuracy:", score[1])

    data_paths_dict = preprocess_data()
    model_data_paths_dict = train_model(data_paths_dict)
    test_model(model_data_paths_dict)


tutorial_mnist_keras_taskflow_api()
