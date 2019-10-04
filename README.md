cookie-shop-serverless
======================

This is an example project for Serverless in AWS

We will be using SAM (https://github.com/awslabs/serverless-application-model)

Most services will be using the free tier so costs should be very minimal.


### Prerequisites:
1. Signup for an AWS account
1. Fork this project into your GitHub account
1. Python 3.7
1. Postman
1. Set up a virtual environment
1. Install dependancies
    * boto3
    * aws-dynamodb-parser
    * coverage


### Activity:

1. Run unit tests `coverage run --branch --source='.' -m unittest` and coverage with `coverage report -m --fail-under=100 --omit=*/__init__.py,tests/*,cookie-shop-env/*` 
1. Run the setup-template.yaml in AWS Cloudformation (give the S3 bucket a globally unique name)
1. Explore the created resources in AWS - S3 bucket, IAM
1. Create a CodeBuild project
    * Connect your GitHub fork
    * This sets up our CI/CD pipeline
1. Run the build
    * This build should create a new Cloudformation stack and create all the resources for us
1. Explore the created resources in AWS - Dynamo, Lambda, API Gateway, IAM
1. Use the API's
    * Go to API Gateway -> Stages -> Prod and get the Invoke URL
    * Use swagger to figure out what to send the API, then postman to call it
    * Try the /cookies and /orders
    * Check Dynamo tables and see your things
    * When an order is placed it will update the quantity of cookies left
1. Add authentication
    * Uncomment the authentication stuff in template.yaml and swagger.yaml
    * The orders endpoint is now protected by IAM (AWS sigv4)
    * To use, go to IAM User, create an access key and secret, then add to the request
