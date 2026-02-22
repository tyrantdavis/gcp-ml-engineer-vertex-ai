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

## Immediate Next Step (Recommended)

### Recommended Action
- Begin preparations for integrating a real trained model into Vertex AI deployment.
- Replace `dummy_model` in `05_deploy_vertex.ipynb` with the trained model artifacts once available.
- Verify local saving and serialization using `.keras` format before attempting endpoint deployment.

### Purpose
- This step advances Course 10 learning objectives without consuming quota.
- Ensures your environment and notebook workflow are ready for live deployment when quota is granted.

### Artifact Updates
- `notebooks/05_deploy_vertex.ipynb`: ready to swap dummy model for actual trained model.
- Local artifacts directory: ready to store serialized `.keras` models.
- Deployment workflow documented, dry-run endpoint placeholder verified.

### Notes
- No actual Vertex AI endpoint creation is performed at this stage to avoid quota consumption.
- All subsequent live deployment steps remain deferred and are captured in the “Deferred / Non-Blocking Notes” section.

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
