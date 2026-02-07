# Colab → GCP ML Engineer Bootstrap (Required)

This repository assumes work is performed in **Google Colab** as part of the
GCP Professional Machine Learning Engineer certification path.

Before running any lab, experiment, or notebook, you **must** execute the
bootstrap notebook.

---

## Purpose

The bootstrap notebook establishes a safe, repeatable environment by:

- Configuring Git commit identity (GitHub noreply)
- Authenticating the user to Google Cloud
- Optionally setting the active GCP project
- Verifying access to a long-lived sandbox GCS bucket
- Installing baseline ML engineering libraries

It does **not**:
- Create or delete GCP resources
- Store secrets
- Train models
- Deploy infrastructure

---

## When to Run

Run the bootstrap notebook:

- At the start of **every new Colab session**
- Before resuming work after a disconnect
- Before committing changes back to GitHub

Colab environments are ephemeral — nothing persists between sessions.

---

## Files

| File | Description |
|----|----|
| `bootstrap_colab_gcp_ml.ipynb` | Canonical environment initialization |
| `BOOTSTRAP_COLAB_GCP_ML.md` | Usage contract and rules |

Do not modify the bootstrap notebook per lab.

---

## GCP Project Safety

Project selection is **opt-in** and controlled by a flag inside the notebook.

Authentication alone is safe and does not incur cost.

---

## Scope

This bootstrap is intentionally scoped to:

- Google Cloud
- Vertex AI
- GCP ML Engineer certification work

It is not intended as a general-purpose ML environment.

---

## Rule of Thumb

If you are about to:
- load data
- train a model
- deploy something

…and the bootstrap notebook hasn’t been run yet — stop and run it first.
