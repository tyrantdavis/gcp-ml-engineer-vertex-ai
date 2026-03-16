import logging

from mlops.pipelines.train_container_pipeline import main as run_training_pipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info("Starting ML pipeline...")
    run_training_pipeline()
    logger.info("Pipeline finished successfully")


if __name__ == "__main__":
    main()
