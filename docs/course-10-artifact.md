# Course 10 Artifact — Vertex AI Model Deployment

## Overview
This document records the progress and artifacts associated with **Module 10 — Vertex AI Model Deployment** in the GCP ML Engineer Path. It documents the steps taken to implement a deployment workflow while respecting quota and resource constraints.

---

## Sections Executed

### 1. Environment Setup & Authentication
- Google Cloud authentication via Colab
- Verified project and GCS bucket
- Installed and initialized Vertex AI SDK (`google-cloud-aiplatform`)

### 2. Dummy Model Deployment (Local)
- Created a **dummy Keras model** (10 input features → 1 output)
- Compiled and saved locally to `artifacts/module10_dummy_model`
- Conducted local predictions to validate workflow

### 3. Vertex AI Endpoint Setup (Dry Run)
- Demonstrated **endpoint creation workflow**
- Placeholder code executed without actual deployment
- Endpoint name used: `module10-dummy-endpoint`

### 4. Test Predictions
- Ran local inference using dummy inputs
- Verified pipeline correctness for **input → model → prediction**

---

## Deployment Artifact Reference

This course includes a quota-safe deployment walkthrough using a placeholder model.

**Notebook:**  
`05_deploy_vertex.ipynb`

**Purpose:**  
Demonstrates Vertex AI deployment mechanics without consuming managed training or serving quota.  
Validates SDK initialization, model serialization, and endpoint configuration patterns. 

---

## Course 10 Artifact Status Update

**Course 10 Artifact Status Update:**  
As of now, `01_exploration.ipynb` and `02_feature_engineering.ipynb` are **pending** and need to be fully populated with EDA and feature engineering steps. `03_training_keras_vertex.ipynb` is ready to proceed once features are prepared. `04_vertex_ai_managed_training.ipynb` is committed and included in the repo. Deployment (`05_deploy_vertex.ipynb`) and production system design (`06_course_production_ml_systems.ipynb`) remain **pending**. Completion of the first two notebooks is required before considering Course 10 fully complete; once done, a new tag (`course-10-complete`) should be created to mark milestone completion.

---

## Course 10 – Immediate Next Steps (Updated)

## 1. 01_exploration.ipynb
- **Status:** Pending  
- **Action:** Populate with full **EDA**: data inspection, summary statistics, visualizations, missing value analysis, and initial insights.  
- **Goal:** Provide a complete understanding of the raw data before any feature prep.  

## 2. 02_feature_engineering.ipynb
- **Status:** Pending  
- **Action:** Populate with **feature preparation**: encoding categorical variables, scaling/norm, creating derived features, and preparing dataset for model training.  
- **Goal:** Produce clean, ready-to-use features for `03_training_keras_vertex.ipynb`.  

## 3. 03_training_keras_vertex.ipynb
- **Status:** Ready once features are prepared  
- **Action:** Continue with model training using prepared features.  

## 4. 04_vertex_ai_managed_training.ipynb
- **Status:** Ensure committed and included in repo (already done).  

## 5. 05_deploy_vertex.ipynb
- **Status:** Pending deployment steps; execute after training completed.  

### Deployment Dry-Run Guidance (Deferred / Non-Blocking)
- **Recommended Action:**  
  - Begin preparations for integrating a real trained model into Vertex AI deployment.  
  - Replace `dummy_model` in `05_deploy_vertex.ipynb` with the trained model artifacts once available.  
  - Verify local saving and serialization using `.keras` format before attempting endpoint deployment.  

- **Purpose:**  
  - Advances Course 10 learning objectives without consuming quota.  
  - Ensures your environment and notebook workflow are ready for live deployment when quota is granted.  

- **Artifact Updates:**  
  - `notebooks/05_deploy_vertex.ipynb`: ready to swap dummy model for actual trained model.  
  - Local artifacts directory: ready to store serialized `.keras` models.  
  - Deployment workflow documented, dry-run endpoint placeholder verified.  

- **Notes:**  
  - No actual Vertex AI endpoint creation is performed at this stage to avoid quota consumption.  
  - All subsequent live deployment steps remain deferred and are captured in the “Deferred / Non-Blocking Notes” section.  

## 6. 06_course_production_ml_systems.ipynb
- **Status:** Pending integration and production system design.  

---

## Note
✅ **Reminder:** Do **not** consider Course 10 “complete” until `01_exploration.ipynb` and `02_feature_engineering.ipynb` are fully executed, committed, and reviewed. Once done, create a **new tag** (`course-10-complete`) to mark the milestone.  

---

### Completion Trigger

When both `01_exploration.ipynb` and `02_feature_engineering.ipynb` are fully executed, committed, and reviewed:

1. Verify training notebook reflects final feature pipeline.
2. Confirm no dummy artifacts remain in deployment notebook.
3. Create annotated tag:
   git tag -a course-10-complete -m "Course 10 complete: EDA, feature engineering, training, and deployment prep finalized."
4. Push tag:
   git push origin course-10-complete

---

## Reminder
- [ ] 01_exploration.ipynb – Pending / initial EDA
- [ ] 02_feature_engineering.ipynb – Pending / feature prep
- [ ] 03_training_keras_vertex.ipynb – Ready once features are prepared

---

## Deferred / Non-Blocking Notes

The following steps are intentionally deferred and **not required** for Course 10 completion:

- Replace `dummy_model` with a trained production model
- Deploy model to a live Vertex AI endpoint once quota permits
- Issue real prediction requests against the endpoint
- Capture serving logs and outputs for operational review

This artifact is considered complete for learning and exam preparation purposes.

---

## Blocking / Deferred Items

### Quota / Service Dependencies
- Real Vertex AI endpoint deployment **requires available quota**
- Currently deferred due to potential quota limitations

### Next Actions (Deferred)
- Deploy trained model once quota allows
- Validate predictions on deployed endpoint
- Record outputs and logs in this artifact document

---

## Notes
- All code executed locally within Colab
- No resource quotas consumed during dummy deployment
- This scaffold ensures **ready-to-execute deployment steps** once real models and quota are available

---

## Exam Relevance
- Demonstrates correct Vertex AI deployment workflow
- Shows readiness for both **local and managed deployment**
- Prepares for integration testing and logging for production ML pipelines
