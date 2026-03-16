import os
from pathlib import Path

ENV = os.getenv("ML_ENV", "local")

ENV_CONFIG = {
    "local": {"artifact_root": "artifacts"},
    "staging": {"artifact_root": "artifacts-staging"},
    "prod": {"artifact_root": "artifacts-prod"},
}

ARTIFACT_ROOT = ENV_CONFIG[ENV]["artifact_root"]

REPO_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = REPO_ROOT / "data"
ARTIFACT_DIR = REPO_ROOT / ARTIFACT_ROOT

TRAIN_DATA = DATA_DIR / "raw" / "train.csv"

MODEL_PATH = ARTIFACT_DIR / "model.keras"
