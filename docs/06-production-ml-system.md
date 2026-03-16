# Production ML System Architecture

This repository demonstrates a simplified but production-oriented machine learning platform architecture.

The goal is to illustrate the complete lifecycle of a machine learning system from data ingestion through model deployment and monitoring.

This document expands on the concepts introduced in:
- notebooks/06_course_production_ml_system.ipynb

```mermaid
flowchart LR

A[Notebooks / Experiments] --> B[Training Container]
B --> C[Model Training Script]

C --> D[Versioned Model Artifacts]
D --> E[Model Metadata Registry]

E --> F[Deployment Pipeline]

F --> G[Serving Infrastructure]
```

---
# End-to-End ML Lifecycle

Modern machine learning systems are typically organized around a lifecycle that transforms raw data into deployed models.

The core lifecycle is:
- Data → Features → Training → Model Registry → Deployment → Monitoring


Each stage represents a distinct responsibility within a production ML platform.

```mermaid
flowchart LR

A[Raw Data] --> B[Feature Engineering]
B --> C[Model Training]
C --> D[Model Registry]
D --> E[Deployment Pipeline]
E --> F[Monitoring]
```
---

## Lifecycle Stages
Data Layer

The data layer provides the raw inputs used for training and evaluation.

Examples include:

- data warehouses

- data lakes

- streaming data sources

In this repository the dataset is simplified, but in real systems this stage often includes:

- data validation

- schema management

- versioned datasets

## Feature Engineering

Feature engineering transforms raw data into model-ready representations.

Typical responsibilities include:

- feature transformations

- feature normalization

- feature selection

Production ML systems frequently use feature stores to manage these transformations.

## Model Training

Training produces models from feature data.

In this repository training occurs inside a containerized environment located in:

training/

Key characteristics:

- reproducible dependencies

- portable execution environment

- compatibility with cloud training systems

## Model Registry

Once training completes, models are stored in a registry.

In this repository the registry is implemented using structured artifact storage:

- artifacts/models/
- artifacts/metadata/

Each training run produces:

- a versioned model artifact

- metadata describing the training run

This provides traceability between training runs and deployed models.

## Deployment

Deployment prepares trained models for serving in production systems.

The deployment pipeline is implemented in:

- mlops/pipelines/deploy_model_pipeline.py

This pipeline identifies the most recent trained model and prepares it for serving infrastructure.

## Monitoring

After deployment, models must be monitored to ensure prediction quality and system health.

Production ML monitoring typically includes:

- prediction data drift detection
- model performance degradation tracking
- service latency and reliability monitoring

In full ML platforms these capabilities are often implemented using systems such as model monitoring services, metrics collection, and alerting infrastructure.

Monitoring infrastructure is not implemented in this repository because the system does not include a live prediction service. However, monitoring represents the final stage of the ML lifecycle and would normally operate downstream of the deployment pipeline.

---

## Repository Architecture

The repository implements a simplified production-style architecture.

```mermaid
flowchart LR

A[Notebooks / Experiments] --> B[Training Container]
B --> C[Model Training Script]

C --> D[Versioned Model Artifacts]
D --> E[Model Metadata Registry]

E --> F[Deployment Pipeline]

F --> G[Serving Infrastructure]
```

---

## Repository Structure
- notebooks/        experimentation
- src/              reusable ML code
- training/         containerized training
- mlops/            pipeline orchestration
- artifacts/        model registry
- docs/             architecture and design documentation

---

## Pipeline Execution

The ML platform orchestration entrypoint is:

- python -m mlops.run_pipeline

Execution flow:

run_pipeline
      ↓
training pipeline
      ↓
training container
      ↓
model artifact + metadata
      ↓
deployment pipeline

---

## Environment Support

The platform supports multiple execution environments:

- local
- staging
- prod

Environment selection is controlled by:

ML_ENV

Example:

ML_ENV=staging python -m mlops.run_pipeline

---

## Summary

This repository demonstrates the major components of a production machine learning platform:

- containerized model training

- pipeline orchestration

- artifact versioning

- deployment pipeline

- multi-environment support

The system illustrates the full ML lifecycle from data processing to model deployment.
