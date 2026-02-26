## ML Notebook Workflow (Quick Reference)

**Execution Order:** 01 → 02 → 03

1. **01_exploration.ipynb**  
   - Explore raw dataset.  
   - Identify feature distributions, missingness, and correlations.  
   - Output: insights for feature engineering.

2. **02_feature_engineering.ipynb**  
   - Clean and transform features.  
   - Save processed dataset locally and optionally to GCS (`DATA_PREP_PREFIX/train_processed.csv`).  
   - Best Practices:
     - Run `auth.authenticate_user()` for GCS access.
     - Local save is authoritative; GCS push is optional but portfolio-aligned.

3. **03_training_keras_vertex.ipynb**  
   - Load processed dataset (`DATA_PREP_PREFIX/train_processed.csv`).  
   - Train Keras classifier.  
   - Evaluate:
     - Accuracy
     - ROC-AUC
     - Confusion Matrix
     - ROC curve + threshold analysis
   - Save model locally (`artifacts/training/model.keras`) and optionally to GCS (`TRAINING_PREFIX`).  
   - Portfolio-grade structure: initialization → dataset load → train → evaluate → save.

**Notes:**  
- Environment variables (`PROJECT_ID`, `DATA_PREP_PREFIX`, `TRAINING_PREFIX`, etc.) are critical.  
- Always maintain **01 → 02 → 03** sequence.  
- Optional GCS uploads require proper authentication (`auth.authenticate_user()`).
