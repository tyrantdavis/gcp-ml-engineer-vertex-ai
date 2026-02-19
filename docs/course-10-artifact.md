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
