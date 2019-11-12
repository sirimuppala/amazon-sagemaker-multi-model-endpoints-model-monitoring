#!/bin/bash
#
# Set the environmental variables to use SageMaker Multi-Model configuration
# with MXNet Model Server (MMS)

# Get the listen port from the SM env variable, otherwise default to 8080
export SAGEMAKER_BIND_TO_PORT=${SAGEMAKER_BIND_TO_PORT:-8080}
# Set custom handler to process model load and inference requests for all models on the container
export SAGEMAKER_HANDLER="/home/model-server/model_handler.py:handle"
export SAGEMAKER_MAX_REQUEST_SIZE=5242880  # Unit: bytes
export SAGEMAKER_MAX_RESPONSE_SIZE=5242880 # Unit: bytes
# Use root as the model store path to allow specifying the full path in the MMS load API calls
export SAGEMAKER_MODEL_STORE=/
export SAGEMAKER_NUM_MODEL_WORKERS=1
export SAGEMAKER_RESPONSE_TIMEOUT=60 # Unit: seconds
