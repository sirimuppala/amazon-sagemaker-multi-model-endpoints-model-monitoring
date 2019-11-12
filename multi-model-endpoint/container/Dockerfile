# Get MMS Base Python 3.6 CPU image on Ubuntu 16.04 base
FROM awsdeeplearningteam/mxnet-model-server:base-cpu-py3.6

# Install MXNet
RUN pip3 install mxnet

# Update MMS installation to get the pre-release version
RUN pip3 install -U --pre --no-cache-dir mxnet-model-server

RUN mkdir -p /home/model-server/

# Copy entrypoint script to the image
COPY dockerd-entrypoint.sh /usr/local/bin/dockerd-entrypoint.sh
RUN chmod +x /usr/local/bin/dockerd-entrypoint.sh

# Copy wrpper script that sets up environment variables to run MMS with SageMaker config
COPY sagemaker_mms_environment_setup.sh /usr/local/bin/sagemaker_mms_environment_setup.sh
RUN chmod +x /usr/local/bin/sagemaker_mms_environment_setup.sh

# Copy the default custom service file to handle incoming data and inference requests
COPY model_handler.py /home/model-server/model_handler.py

# Expose container port for management and inference requests
EXPOSE 8080

# Define an entrypoint script for the docker image
ENTRYPOINT ["/usr/local/bin/dockerd-entrypoint.sh"]

# Define command to be passed to the entrypoint
CMD ["serve"]

# Set a docker label to advertise multi-model support on the container
LABEL com.amazonaws.sagemaker.capabilities.multi-models=true
# Set a docker label to enable container to use SAGEMAKER_BIND_TO_PORT environment variable if present
LABEL com.amazonaws.sagemaker.capabilities.accept-bind-to-port=true

