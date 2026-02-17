import os

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Env vars injected by Vertex
PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
OUTPUT_DIR = os.environ.get("AIP_MODEL_DIR")  # REQUIRED by Vertex


def main():
    # Dummy dataset
    X_train = np.random.rand(1000, 10)
    y_train = np.random.randint(0, 2, size=(1000,))

    X_val = np.random.rand(200, 10)
    y_val = np.random.randint(0, 2, size=(200,))

    # Minimal model
    model = keras.Sequential(
        [
            layers.Input(shape=(10,)),
            layers.Dense(16, activation="relu"),
            layers.Dense(8, activation="relu"),
            layers.Dense(1, activation="sigmoid"),
        ]
    )

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    # Train
    model.fit(
        X_train,
        y_train,
        validation_data=(X_val, y_val),
        epochs=5,
        batch_size=32,
    )

    # Save is expected by Vertex
    model.save(os.path.join(OUTPUT_DIR, "model.keras"))


if __name__ == "__main__":
    main()
