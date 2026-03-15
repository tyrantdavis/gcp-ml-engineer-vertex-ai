#!/bin/bash

# Build the training container
docker build -t gcp-ml-engineer-vertex-ai-training -f training/Dockerfile .

# Run the container:
    # Persist model output
    # Make dataset accessible

docker run \
-v $(pwd)/artifacts:/app/artifacts \
-v $(pwd)/data:/app/data \
gcp-ml-engineer-vertex-ai-training

# Automate and orchestrate tasks within the containerization workflow
