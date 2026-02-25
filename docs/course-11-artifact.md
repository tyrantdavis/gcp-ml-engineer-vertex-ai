# Course 11 — Artifact Documentation

## Overview

### What
- Tracks all outputs, experiments, and artifacts produced during Course 11
  of the GCP ML Engineer learning path.
- Serves as the canonical reference for notebooks, design artifacts, and
  production ML system workflows.

### Why
- Maintains continuity across the learning path.
- Provides a structured, exam-relevant record for future reference and review.

---

## Sections Executed

### What
- Lists each notebook or module associated with Course 11.
- Provides a brief description of purpose and learning objective.

### Why
- Ensures all learning steps are traceable.
- Supports exam preparation and post-course review.

| Notebook                               | Purpose                                              | Status              |
|----------------------------------------|------------------------------------------------------|---------------------|
| 06_course_production_ml_systems.ipynb  | Production ML system design & orchestration (concept)| Complete            |
| 07_course11_.ipynb                     | Reserved / optional                                  | Not required        |

---

## Experiments & Models

### What
- Documents datasets, preprocessing, and models referenced during Course 11.
- Includes local paths and (if applicable) GCS URIs.

### Why
- Ensures reproducibility and traceability.
- Validates learning objectives without requiring live execution.

| Model / Artifact | Description                                | Local / GCS Path                          | Status   |
|------------------|--------------------------------------------|-------------------------------------------|----------|
| dummy_model      | Conceptual placeholder (design-only)       | artifacts/course11/dummy_model.keras      | Complete |
| <real_model>     | Intentionally deferred                     | artifacts/course11/<model>.keras          | Deferred |

---

## Deployment / Optional

### What
- Tracks optional deployment-related steps (design-level only).
- Includes dry-run or quota-deferred deployment notes.

### Why
- Demonstrates understanding of deployment workflows.
- Avoids unnecessary quota or cost consumption.

| Deployment               | Notes                                      | Status   |
|--------------------------|--------------------------------------------|----------|
| Vertex AI Endpoint       | Design-only; quota-deferred                | Deferred |

---

## Deferred / Non-Blocking Notes

### What
- Captures steps intentionally deferred due to quota, scope, or cost discipline.

### Why
- Keeps the learning record complete without blocking progress.

- Replace dummy models with trained models when available.
- Deploy to Vertex AI endpoints once quota permits.
- Record live logs, metrics, and outputs if executed in the future.

---

## Scope & Intent (Explicit)

### What this course covers
- Production ML system design and reasoning.
- Separation of concerns across:
  - Training logic
  - Pipeline orchestration
  - Deployment configuration
  - Monitoring and governance
- End-to-end lifecycle thinking from data ingestion to monitoring.

### What this course intentionally does not do
- Execute live training jobs.
- Deploy live Vertex AI endpoints.
- Consume managed training or serving quota.

This course is design-first by intent.

---

## Artifact References

- notebooks/06_course_production_ml_systems.ipynb  
  Conceptual production ML system walkthrough (non-executing)

- training/trainer/task.py  
  Trainer responsibility boundary

- mlops/pipelines/training_pipeline.py  
  Pipeline orchestration logic

- deployment/endpoint_config.yaml  
  Deployment configuration abstraction

- docs/architecture.md  
  System-level architecture reference

---

## Exam Framing

This course maps directly to exam expectations around:
- System boundaries and ownership
- Failure modes and recovery paths
- Reproducibility and auditability
- Cost-aware ML system design
- Monitoring and drift awareness

---

## Course 11 Close-Out Summary

### What
- Establishes a complete, design-level production ML system skeleton.
- Documents system reasoning without requiring live execution.

### Why
- Aligns with exam expectations.
- Preserves cost discipline.
- Enables future extension without rework.