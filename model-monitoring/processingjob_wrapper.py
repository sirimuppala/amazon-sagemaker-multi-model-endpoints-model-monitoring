import boto3

class ProcessingJob(object):
    def __init__(self, sm_client, role_arn, instance_type='ml.m5.xlarge',  instance_count=1, volume_size=20):
        self.sm_client = sm_client
        self.role_arn = role_arn
        self.instance_type = instance_type
        self.instance_count = instance_count
        self.volume_size = volume_size

    def create(self, job_name, input_s3_uri, output_s3_uri):
        print('Creating ProcessingJob {}...'.format(job_name))
        job = self.sm_client.create_processing_job(
                            ProcessingInputs = [
                                {
                                    'InputName': 'input',
                                    'S3Input': {
                                        'S3Uri': input_s3_uri,
                                        'LocalPath': '/opt/ml/processing/sm_input',
                                        'S3DataType': 'S3Prefix',
                                        'S3InputMode': 'File',
                                        'S3DataDistributionType': 'FullyReplicated',
                                        'S3CompressionType': 'None'
                                    }                                                                
                                }
                            ],
                            ProcessingOutputConfig = {
                                'Outputs': [
                                    {
                                        'OutputName': 'results',
                                        'S3Output': {
                                            'S3Uri': output_s3_uri,
                                            'LocalPath': '/opt/ml/processing/sm_output',
                                            'S3UploadMode': 'EndOfJob'
                                        }
                                    }
                                ]
                            },
                            ProcessingJobName =  job_name,
                            ProcessingResources = {
                                'ClusterConfig': {
                                    'InstanceCount': self.instance_count,
                                    'InstanceType': self.instance_type,
                                    'VolumeSizeInGB': self.volume_size
                                }
                            },
                            StoppingCondition = {
                                'MaxRuntimeInSeconds': 3600
                            },
                            AppSpecification = {
                                'ImageUri': '159807026194.dkr.ecr.us-west-2.amazonaws.com/sagemaker-model-monitor-analyzer',
                            },
                            Environment = {
                                'dataset_source': '/opt/ml/processing/sm_input',
                                'dataset_format' : '{\"csv\": {\"header\" :  true}}',
                                'output_path' : '/opt/ml/processing/sm_output',
                                'publish_cloudwatch_metrics' : 'Disabled'                            
                            },
                            RoleArn =  self.role_arn
        )   
        return job