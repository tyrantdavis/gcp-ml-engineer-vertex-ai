import json
import logging
from pathlib import Path

from src.config import ARTIFACT_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

METADATA_DIR = ARTIFACT_DIR / "metadata"


def get_latest_model():
    metadata_files = sorted(METADATA_DIR.glob("model_*.json"))
    latest_meta = metadata_files[-1]

    with open(latest_meta) as f:
        metadata = json.load(f)

    return metadata["model_path"]


def main():
    model_path = get_latest_model()

    logger.info(f"Deploying latest model: {model_path}")

    # Placeholder for real deployment step
    logger.info("Model ready for deployment pipeline")


if __name__ == "__main__":
    main()
