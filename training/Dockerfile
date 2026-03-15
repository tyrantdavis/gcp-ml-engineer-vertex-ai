FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt && pip cache purge

COPY training/trainer ./trainer

RUN mkdir -p /app/artifacts

# Training entrypoint
ENTRYPOINT ["python", "trainer/task.py"]

# What This Does
# Defines reproducible training environment
# Installs the same dependencies used by the notebooks
# Runs training through a standard Python entrypoint
