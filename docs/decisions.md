# Engineering Decisions

This document records key architectural decisions made while designing the production ML platform in this repository.

The goal of the system was to demonstrate a realistic ML platform architecture while maintaining simplicity and clarity.

---

# Decision 1 — Containerized Training

## Decision

Model training is executed inside a Docker container.

## Why

Containerized training provides:

- reproducible environments
- consistent dependency management
- portability between local execution and cloud platforms

This approach mirrors training workflows used in production ML systems.

---

# Decision 2 — Pipeline-Based Execution

## Decision

Training and deployment workflows are orchestrated through pipelines located in: mlops/pipelines/


## Why

Separating orchestration from model code allows:

- cleaner architecture
- easier automation
- better CI/CD integration

This pattern is widely used in modern ML platforms.

---

# Decision 3 — Lightweight Model Registry

## Decision

Model artifacts and metadata are stored in structured directories:
artifacts/models/
artifacts/metadata/


Each training run produces:

- a timestamped model artifact
- a metadata file describing the training run

## Why

This introduces traceability and versioning without requiring an external system.

It demonstrates the core behavior of a model registry while keeping the repository self-contained.

---

# Decision 4 — Multi-Environment Support

## Decision

The platform supports multiple environments via the `ML_ENV` environment variable.

Available environments:


local
staging
prod


## Why

Production ML systems rarely operate in a single environment.

Environment separation enables:

- safe testing of pipelines
- controlled deployment workflows
- configuration isolation

---

# Decision 5 — CI Validation of Training Environment

## Decision

A GitHub workflow builds and runs the training container on repository updates.

## Why

This ensures:

- dependency reproducibility
- container build stability
- early detection of training failures

Automated validation is a core requirement in production ML systems.

---

# Decision 6 — Modular Repository Layout

## Decision

The repository separates responsibilities into distinct directories.


notebooks/
src/
training/
mlops/
artifacts/
docs/


## Why

This structure mirrors the separation of concerns found in large ML codebases.

It improves maintainability and allows experimentation, training, and orchestration logic to evolve independently.

---

# Summary

These decisions collectively produce a system that demonstrates the core components of a production ML platform while remaining simple enough to understand and extend.
