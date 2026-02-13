# Course 9 Artifact — Keras on Vertex AI
## Certification Context

**Certification**: Google Cloud Professional Machine Learning Engineer
**Course**: Build, Train and Deploy ML Models with Keras on Google Cloud (Course 9)

This document describes the portfolio artifact produced for Course 9. The goal of this artifact is to demonstrate correct ML engineering fundamentals prior to introducing managed training, pipelines, or MLOps automation.

### Artifact Location

Primary implementation:

- notebooks/03_training_keras_vertex.ipynb

Supporting documentation:

- notebooks/README.md
### Artifact Objective

The objective of this artifact is to validate that:

- A Keras model can be defined correctly

- Training logic functions end-to-end

- Artifacts can be serialized reliably

- Failures can be isolated to code vs environment vs IAM

This artifact intentionally prioritizes **correctness and debuggability** over scale.

### What the Artifact Demonstrates
#### 1. Environment Configuration

- Uses environment variables for project, bucket, and paths

- Avoids hard-coded identifiers

- Mirrors production-safe configuration patterns

#### 2. Dummy Dataset (Local)

- Synthetic dataset generated locally

- Used solely to validate training mechanics

- Eliminates data dependency as a failure source

#### 3. Minimal Keras Model

- Simple feed-forward neural network

- Appropriate activations and loss for binary classification

- Explicit compilation and model summary

#### 4. Local Sanity Run (Critical)

Model trained locally for a small number of epochs

- Confirms:

  - data flow

  - gradient updates

  - loss convergence

This step is mandatory before any cloud-based training.

#### 5. Artifact Persistence

- Model saved using native Keras format (.keras)

- Local artifact directory treated as authoritative

- GCS persistence documented but optional due to IAM constraints

## What This Artifact Intentionally Excludes

To maintain clarity of responsibility, the following are explicitly out of scope:

- Vertex AI custom training jobs

- Hyperparameter tuning

- Pipelines

- CI/CD integration

- Model deployment

These concerns are addressed in later courses focused on production ML systems.

## Notes on IAM and GCS Access

In managed lab environments, permissions for writing to Google Cloud Storage may be restricted.

When GCS write access is unavailable:

- Local artifact persistence is considered sufficient

- The workflow remains valid

- The limitation is attributed to IAM, not implementation error

This mirrors real-world enterprise constraints.

Why This Artifact Matters

This artifact establishes a clean engineering baseline:

- Later Vertex AI failures can be confidently attributed to platform configuration

- Model behavior is already validated

- Artifact formats are already known-good

In professional ML systems, skipping this step increases debugging cost exponentially.

## Next Steps

Subsequent artifacts will build on this foundation to introduce:

- Managed training with Vertex AI

- Evaluation and monitoring

- MLOps pipelines

- Deployment patterns

This artifact remains frozen and serves as a reference point for all future work.
