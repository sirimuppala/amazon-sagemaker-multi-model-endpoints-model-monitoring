import boto3

from sagemaker.utils import name_from_base

class MonitoringSchedule(object):
    def __init__(self, sm_client, role_arn, instance_type="ml.m5.xlarge",  instance_count=1, volume_size=20):
        self.sm_client = sm_client
        self.role_arn = role_arn
        self.instance_type = instance_type
        self.instance_count = instance_count
        self.volume_size = volume_size

    def create(self, schedule_name, 
               endpoint_name, 
               output_s3_uri, 
               record_preprocessor_source_uri='', 
               post_analytics_source_uri='',
               baseline_constraints_uri='',
               baseline_statistics_uri=''
               ):
        print('Creating Monitoring Schedule {}...'.format(schedule_name))
        schedule = self.sm_client.create_monitoring_schedule(
            MonitoringScheduleName = schedule_name,
            MonitoringScheduleConfig = {
                'ScheduleConfig': {
                    # every hour
                    'ScheduleExpression': 'cron(0 * * * ? *)'
                    # every 10 minutes
                    # 'ScheduleExpression': "cron(0/10 * * * ? *)"
                },
                'MonitoringJobDefinition': {
                    'BaselineConfig': {
                        'ConstraintsResource': {
                            'S3Uri': baseline_constraints_uri
                        },
                        'StatisticsResource': {
                            'S3Uri': baseline_statistics_uri
                        }
                    },
                    'MonitoringInputs': [
                        {
                            'EndpointInput': {
                                'EndpointName': endpoint_name,
                                'LocalPath': '/opt/ml/processing/sm_input',
                                'S3InputMode': 'File',
                                'S3DataDistributionType': 'FullyReplicated'
                            }
                        }
                    ],
                    'MonitoringOutputConfig': {
                        'MonitoringOutputs': [
                            {
                                'S3Output': {
                                    'S3Uri': output_s3_uri,
                                    'LocalPath': '/opt/ml/processing/sm_output',
                                    'S3UploadMode': 'EndOfJob'
                                }
                            }
                        ]
                    },
                    'MonitoringResources': {
                        'ClusterConfig': {
                            'InstanceCount': self.instance_count,
                            'InstanceType': self.instance_type,
                            'VolumeSizeInGB': self.volume_size
                        }
                    },
                    'MonitoringAppSpecification': {
                        # beta - 922956235488.dkr.ecr.us-west-2.amazonaws.com/sagemaker-model-monitor-analyzer
                        # gamma - 894667893881.dkr.ecr.us-west-2.amazonaws.com/sagemaker-model-monitor-analyzer
                        # alpha - 304864522798.dkr.ecr.us-west-2.amazonaws.com/sagemaker-model-monitor-analyzer:latest
                        # pdx prod - 159807026194.dkr.ecr.us-west-2.amazonaws.com/sagemaker-model-monitor-analyzer:latest
                        'ImageUri': '159807026194.dkr.ecr.us-west-2.amazonaws.com/sagemaker-model-monitor-analyzer',
                        #'RecordPreprocessorSourceUri' : record_preprocessor_source_uri,
                        'PostAnalyticsProcessorSourceUri' : post_analytics_source_uri
                    },
                    #'StoppingCondition': {
                     #   'MaxRuntimeInSeconds': 600000
                    #},
                    #'Environment: {
                    #    'KeyName': ''
                    #},
                    'RoleArn': self.role_arn
                }
            }
        )   
        return schedule
