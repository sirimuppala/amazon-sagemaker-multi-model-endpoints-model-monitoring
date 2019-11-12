#!/bin/bash
set -e # fail script on any individual command failing
set -x # echo commands executed

if [[ "$1" = "serve" ]]; then
 shift 1
 
 # Load SageMaker Multi-Model environment variables
 source sagemaker_mms_environment_setup.sh

 # Start the MMS server with sagemaker config
 mxnet-model-server --start --mms-config sagemaker
else
 eval "$@"
fi

# prevent docker exit
tail -f /dev/null
