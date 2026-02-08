# train.py — Canonical Training Script for Vertex AI

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os
import sys

# ======================
# Configuration (from notebook or env)
# ======================
train_csv = sys.argv[1] if len(sys.argv) > 1 else "gs://ml-cert-sandbox-bucket-js-001/training/train.csv"
output_dir = os.getenv("AIP_MODEL_DIR", "/tmp/model/")  # Vertex AI injects this env var

os.makedirs(output_dir, exist_ok=True)

# ======================
# Load Data
# ======================
df = pd.read_csv(train_csv)
X = df.drop(columns=["target"])
y = df["target"]

# ======================
# Train/Test Split
# ======================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ======================
# Train Model
# ======================
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ======================
# Evaluate
# ======================
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Validation Accuracy: {acc:.4f}")

# ======================
# Save Model
# ======================
model_path = os.path.join(output_dir, "model.joblib")
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")
