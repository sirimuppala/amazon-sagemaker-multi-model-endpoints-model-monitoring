# amazon-sagemaker-multi-model-endpoints-model-monitoring

# Preparation
<details>
  <summary>Click to expand!</summary>
  
  ### Step 1 - Setup

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
* pretrained models : Notebooks for training movie and music recommendation models.  Models trained will be saved to an S3 buckets and will be made available.  These files will NOT be used for the deployment workshop.
* model-monitoring : Notebook(s) to demonstrate the model monitoring / data capture functionality
* multi-model-endpoint : Notebook(s) and supporting code for deploying both movie and music recommendation models behind a single endpoint.

# High Level Steps

* Explore Model Monitoring and Data Capture
  
  Use RhineStone to explore model-monitoring and data capture. (Waiting on access to put together the whole sequence)
  
  (For now - Execute model-monitoring/monitor_xgboost_recommendation_model.ipynb

* Explore hosting multiple models behind a single endpoint

  TBD : Can we use Rhinestone to explore this?
  
  (For now - Execute multi-model-endpoint/multiple_recommendation_models_endpoint.ipynb)