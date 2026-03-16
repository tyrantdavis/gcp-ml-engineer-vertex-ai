import logging
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parents[2]
IMAGE_NAME = "gcp-ml-engineer-vertex-ai-training"


def build_training_image():
    logger.info("Building training container image...")
    subprocess.run(
        [
            "docker",
            "build",
            "-t",
            IMAGE_NAME,
            "-f",
            "training/Dockerfile",
            ".",
        ],
        cwd=REPO_ROOT,
        check=True,
    )


def run_training_container():
    logger.info("Running training container...")
    subprocess.run(
        [
            "docker",
            "run",
            "-v",
            f"{REPO_ROOT}/artifacts:/app/artifacts",
            "-v",
            f"{REPO_ROOT}/data:/app/data",
            IMAGE_NAME,
        ],
        cwd=REPO_ROOT,
        check=True,
    )


def main():
    build_training_image()
    run_training_container()
    logger.info("Training pipeline completed successfully.")


if __name__ == "__main__":
    main()
