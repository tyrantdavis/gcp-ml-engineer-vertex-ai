from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = REPO_ROOT / "data"
ARTIFACT_DIR = REPO_ROOT / "artifacts"

TRAIN_DATA = DATA_DIR / "raw" / "train.csv"

MODEL_PATH = ARTIFACT_DIR / "model.keras"
