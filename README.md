cookie-shop-serverless
======================

This is an example project for Serverless in AWS

We will be using SAM (https://github.com/awslabs/serverless-application-model)

Most services will be using the free tier so costs should be very minimal.


### Prerequisites:
1. Signup for an AWS account
1. Fork this project into your GitHub account
1. Python 3.9
1. Postman
1. Set up a virtual environment
1. Install dependancies
    * boto3
    * aws-dynamodb-parser
    * coverage


### Activity:

1. Run unit tests `coverage run --branch --source='.' -m unittest` and coverage with `coverage report -m --fail-under=100 --omit=*/__init__.py,tests/*,cookie-shop-env/*` 
1. Run the setup-template.yaml in AWS Cloudformation
    * Give the S3 bucket a globally unique name (line 78)
    * If this fails it is most likely because Cloudformation cannot setup CodeBuild projects without first connecting to Github through OAuth. You should create a dummy CodeBuild project and connect to Github.
    * Explore the created resources in AWS - S3, IAM, CodeBuild, SSM
1. Create a PR in the repo
    * This build will use buildspec-dev.yaml and should create a new Cloudformation stack (dev) and create all the resources for us.  Note this will be a seperate stack for each PR.
    * Explore the created resources in AWS - Dynamo, Lambda, API Gateway, etc.
1. Use the API's
    * Go to API Gateway -> Stages -> Prod and get the Invoke URL
    * Use swagger to figure out what to send the API, then postman to call it
    * Try the /cookies and /orders
    * Check Dynamo tables and see your things
    * When an order is placed it will update the quantity of cookies left
1. Authentication
    * The orders endpoint is protected by IAM (AWS sigv4)
    * To use, go to the IAM User created, create an access key and secret, then add to the request

# HIYAAAA
