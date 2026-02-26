# GCP ML Engineer Notebook Workflow

This note provides a **high-level reference** for the sequence and dependencies of the notebooks in this repository. It is intended for onboarding, future reference, or cross-notebook troubleshooting.

---

## Notebook Sequence Overview

### 01_exploration.ipynb
**Purpose:** Initial data exploration and analysis.  
**Scope:**
- Import raw dataset.
- Quick descriptive statistics.
- Visualize target distribution and feature correlations.
- Identify missing values and potential feature transformations.
- Save summary insights (not artifacts).

**Outputs / Dependencies:**  
- Understanding of target distribution, missingness, and potential leakage risks.
- Sets expectations for feature engineering in 02.

---

### 02_feature_engineering.ipynb
**Purpose:** Prepare a clean, processed dataset for modeling.  
**Scope:**
- Apply feature engineering (e.g., encoding, transformations, handling missing values).
- Split categorical and numerical features as needed.
- Save processed dataset **locally** and optionally push to GCS using `DATA_PREP_PREFIX`.
- Ensure reproducibility using the Colab secrets environment.

**Best Practices / Notes:**
1. Run `auth.authenticate_user()` before writing to GCS.
2. `DATA_PREP_PREFIX` drives bucket/folder structure; no hardcoding needed.
3. Local save is authoritative for iterative runs.
4. Downstream notebooks can read dataset directly from `DATA_PREP_PREFIX/train_processed.csv`.

**Outputs / Dependencies:**  
- `train_processed.csv` available locally and optionally on GCS.
- Input for 03_training_keras_vertex.ipynb.

---

### 03_training_keras_vertex.ipynb
**Purpose:** Train a minimal Keras model using the processed dataset.  
**Scope:**
- Validate environment and permissions.
- Load processed dataset from `DATA_PREP_PREFIX`.
- Train Keras classifier.
- Evaluate using:
  - Accuracy
  - ROC-AUC
  - Confusion Matrix
  - ROC curve visualization
  - Threshold tuning analysis
- Save model artifacts locally (`artifacts/training`) and optionally push to GCS (`TRAINING_PREFIX`).

**Best Practices / Notes:**
1. Run `auth.authenticate_user()` before any GCS operations.
2. Local artifact save is authoritative; safe for iterative runs.
3. Maintain notebook structure: initialization → dataset load → model training → evaluation → artifact save.
4. Visual metrics provide portfolio-grade evaluation insights.

**Outputs / Dependencies:**  
- Trained Keras model locally (`model.keras`) and optionally on GCS.
- Evaluation metrics and visualizations for portfolio reporting.

---

## General Workflow Notes
- Always follow the **01 → 02 → 03** order.
- Environment variables (`DATA_PREP_PREFIX`, `TRAINING_PREFIX`, `PROJECT_ID`, etc.) are critical for reproducibility.
- Optional GCS pushes ensure portfolio alignment but require correct authentication.
- This note serves as a **central reference**; no code execution happens here.
