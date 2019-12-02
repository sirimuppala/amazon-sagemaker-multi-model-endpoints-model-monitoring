# amazon-sagemaker-multi-model-endpoints-model-monitoring

# Preparation
<details>
  <summary>Click to expand!</summary>
  
  ### Step 1 - Setup

(Note : For ReInvent, the workshop conductors will do this step ahead of time in the event engine)

In this step, you will execute a Cloud Formation template to do some initial setup of our environment including creating:

* SageMaker Notebook Instance: This notebook instance will be used as our lab environment after our initial setups required for setting up the workshop.

* SageMaker Notebook lifecycle configuration: Lifecycle configuration created to automatically clone this workshop repository including the notebook instance included for this workshop.

##### Detailed Steps

1.1. Download this git repository by either cloning the repository or downloading the *zip

1.2. Login to the [AWS Console](https://https://console.aws.amazon.com/) and enter your credentials

1.3. Under **Services**, select search for and select [CloudFormation](https://console.aws.amazon.com/cloudformation)

1.4. Click **Create Stack** buttton

   ![CreateStack](images/CreateStack.png)
   
1.5. Under **Select Template**:
    * Click radio button next to 'Upload a template to Amazon S3', then click **Browse**
    * From the local repository cloned to your machine in the detailed step 1, select the file ./prep/Workshop-Prep.yml
    * Click **Open**
    ![CreateStack](images/CreateStack-SpecifyTemplate.png)
    
1.6. Under **Specify Stack Details**, enter: 

   * **Stack Name**: Enter SageMakerDeploymentOptions

   *  **UniqueID**: Enter *yourinitials* in lower case (Example: jdd)

   ![CreateStack](images/CreateStack-SpecifyStackDetails.png)

1.7. Click **Next**

1.8. Under **Options**, leave all defaults and click '**Next**'

1.9. Under **Review**, scroll to the bottom and check the checkbox acknowledging that CloudFormation might create IAM resources and custom names, then click **Create**

![CreateStack](images/CreateStack-IAMCapabilities.png)

1.10. You will be returned to the CloudFormation console and will see your stack status '**CREATE_IN_PROGRESS**'

![CreateStack](images/CreateStack-CreateInProgress.png)

1.11. After a few minutes, you will see your stack Status change to '**CREATE_COMPLETE**'.  You're encouraged to go explore the resources created as part of this initial setup. 
</details>

# Code organization

* pretrained models : Notebook(s) for training movie and music recommendation models.  Models trained will be saved to an S3 buckets and will be made available.  These files will NOT be used for the deployment workshop.
* model-monitoring : Notebook and supporting to demonstrate the model monitoring / data capture functionality
* multi-model-endpoint : Notebook and supporting code for deploying both movie and music recommendation models behind a single endpoint.

# High Level Steps

* Module 1 : Validate AWS account 
    1. Login to AWS Console using the details provided
    2. Navigate to CloudFormation console
	    
	    * Verify that stack “SageMaker-Deployment-Workshop” is launched.
        
        * Visit the Outputs tab and make note of values for 'SNSTopicARN' and 'S3Bucket'
    3. Navigate to Amazon SageMaker console
    
        * Verify that the SageMaker Notebook instance “DeploymentOptions-Notebook-reinvent” is InService.
        * Click “Open Jupyter”
        * Verify you see models and data directori
    
    
* Module 2 :  Explore Amazon SageMaker Data Capture and Model Monitoring Capabilities

    In this module of the workshop, you will execute various sections of the notebook 
model-monitoring/ monitor_xgboost_recommendation_model.ipynb.

    1. Click on model-monitoring/monitor_xgboost_recommendation_model.ipynb to open it.
    2. Read through the instructions in the notebook and execute cells in the sections below in this order. 
       *  Section I - Setup
       *  Section II - Deploy pre-trained model with model data capture enabled
       *  Section III - Run predictions and analyze data captured
       *  Section IV – Generate baseline statistics and constraints
       *  Section V – Monitor and analyze model for data drift 
       *  Section VI – Retrigger movie recommendation model training 

* Module 3 : Explore Multi Model Endpoints
    In this module of the workshop, you will execute the cells in
multi-model-endpoint/multiple_recommendation_models_endpoint.ipynb. 
    1. Click on multi-model-endpoint/multiple_recommendation_models_endpoint.ipynb to open it.
    2. Read through the instructions in the notebook and execute cells. 
