# Notebooks — GCP ML Engineer (Vertex AI)

This directory contains curated, portfolio-grade notebooks created as part of the Google Cloud Professional Machine Learning Engineer certification path.

These notebooks are not exploratory scratch work. Each one is intentionally scoped to demonstrate a specific ML engineering responsibility aligned with exam domains and real-world GCP workflows.

## Notebook Index
03_training_keras_vertex.ipynb

### Status: ✅ Complete & frozen
### Course: Build, Train and Deploy ML Models with Keras on Google Cloud (Course 9)

### What this notebook does

- Builds a minimal but correct Keras model

- Trains the model locally to validate the ML pipeline

- Performs a local sanity run (required before any cloud training)

- Saves model artifacts in native Keras format (.keras)

 - Demonstrates correct separation of:

  - model training

  - artifact persistence

  - cloud deployment (explicitly deferred)

### What this notebook intentionally does not do

❌ No Vertex AI training jobs

❌ No hyperparameter tuning

❌ No pipelines

❌ No production deployment

Those concerns are addressed in later courses (Production ML Systems, MLOps with Vertex AI).

## Why this notebook exists

This notebook establishes a clean foundation for all subsequent Vertex AI and MLOps work.

Before scaling training or introducing managed services, a professional ML engineer must be able to answer:

Can the model train successfully?

Can artifacts be serialized correctly?

Can failures be attributed to code vs platform vs IAM?

**This notebook answers those questions locally first, which is the correct engineering order of operations.**

## Notes on GCS and IAM (Important)

Saving artifacts to Google Cloud Storage may be restricted in lab environments due to IAM constraints.
When this occurs:

Local artifact saving is treated as the authoritative output

GCS save logic remains documented but intentionally skipped

This reflects real-world constraints and is not a defect in the workflow.

## How to use these notebooks

Run notebooks top-to-bottom in Colab

Do not modify frozen notebooks

Later notebooks may depend on the structure and assumptions established here

If you are reviewing this repository:

Think of these notebooks as engineering checkpoints, not tutorials.

Next notebooks (planned)

Feature engineering and data validation

Vertex AI managed training

Model evaluation and monitoring

MLOps pipelines with Vertex AI
