# Course 9 Artifact — Keras on Vertex AI
---

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

---

## Vertex AI Managed Training — Closure Record

### Scope

This section documents the end-to-end attempt to execute Vertex AI Managed Training (Python package–based) for Course 9 (Keras on Vertex AI), including preparation, execution blockers, and intentional deferral. The objective was to validate a correct managed-training workflow rather than force execution under constrained project quotas.

### Status

- Local environment preparation: complete

- Colab environment preparation: complete

- Repository structure validated for Vertex AI training: complete

- setup.py Python package configuration: complete

- Source distribution build (sdist): complete

- Training package upload to GCS: complete

- Vertex AI Managed Training execution: blocked (quota)

### Implemented Architecture

- Training mode: Vertex AI Managed Training (Python package)

- Entry point: trainer.task

- Packaging: setup.py + source distribution (course9_trainer-0.1.0.tar.gz)

- Artifact storage: Google Cloud Storage

- Execution interface: gcloud ai custom-jobs create

- Environment: Google Colab (authenticated, project-scoped)

All required structural, packaging, and configuration prerequisites for managed training were successfully validated prior to execution.

### Blocking Issue

- Error type: Quota exhaustion

- Service: aiplatform.googleapis.com

- Metric: custom_model_training_cpus

- HTTP status: RESOURCE_EXHAUSTED (429)

- Impact: Prevents job scheduling despite correct configuration

This failure occurred after API enablement and command validation, indicating an external quota constraint rather than a configuration or architectural defect.

### Resolution Decision

- Managed training execution was intentionally deferred

- No further retries attempted to avoid:

  - Repeated quota errors

  - Command churn without new signal

  - Disruption to overall learning velocity

- A quota increase request is the documented resolution path, to be executed only if/when project constraints allow

No code, packaging, or architectural changes are required prior to a future retry.

### Verification Summary

The following were explicitly confirmed during this process:

- Correct usage of Vertex AI–supported Python package training flow

- Proper separation of:

  - Packaging (setup.py, sdist)

  - Storage (GCS)

  - Execution (custom job submission)

- Correct error classification (quota vs. misconfiguration)

- Clean stop with no partial or inconsistent state

### Exam & Portfolio Relevance

This artifact demonstrates:

- - End-to-end knowledge of Vertex AI Managed Training

- - Correct Python package–based training setup

- - Ability to diagnose and distinguish quota failures from configuration errors

- - Professional handling of blocked execution scenarios

- - Real-world GCP operational decision-making (defer vs. force)

The absence of a completed training run is intentional and justified, and does not detract from the architectural or conceptual validity of the implementation.

### Next Action (Deferred)
#### Deferred Retry Path (Non-Blocking)

- Quota increase request for
  `aiplatform.googleapis.com/custom_model_training_cpus` has been queued; project shows 100% usage until GCP approves.
- Managed training job execution is deferred until quota is granted.
- All other artifacts and learning objectives remain unaffected and fully complete.

**Status:**  
Until quota approval, this workstream is considered closed and complete. No additional action is required for progress.
