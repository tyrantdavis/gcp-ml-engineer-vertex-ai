# Training entrypoint inside container
import logging
import os

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Env vars injected by Vertex
PROJECT_ID = os.environ.get("GCP_PROJECT_ID")

# Vertex provides AIP_MODEL_DIR; fallback allows local container runs
OUTPUT_DIR = os.environ.get("AIP_MODEL_DIR", "/app/artifacts")

# Safe directory creation before saving artifacts
os.makedirs(OUTPUT_DIR, exist_ok=True)


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
    model_path = os.path.join(OUTPUT_DIR, "model.keras")
    logger.info(f"Saving model to: {model_path}")
    model.save(model_path)


if __name__ == "__main__":
    main()
