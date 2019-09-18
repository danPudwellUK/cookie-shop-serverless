cookie-shop-serverless
======================

This is an example project for Serverless in AWS

We will be using SAM (https://github.com/awslabs/serverless-application-model)

Most services will be using the free tier so costs should be very minimal.


### Prerequisites:
1. Signup for an AWS account
2. Fork this project into your GitHub account
3. Python 3.7
4. Postman


### Activity:
1. Run the setup-template.yaml in AWS Cloudformation
2. Create a CodeBuild project
    * Connect your GitHub fork
    * This sets up our CI/CD pipeline
3. Run the build
    * This build should create a new Cloudformation stack and create all the resources for us
4. Explore the project and created resources in Dynamo, Lambda, API Gateway, IAM
5. Add a stream to our Orders DynamoDB
    * Uncomment the stream stuff in template.yaml
    * When an order is placed it will now update the quantity of cookies left
6. Add authentication
    * Uncomment the authentication stuff in template.yaml and swagger.yaml
    * The orders endpoint is now protected by IAM (AWS sigv4)
    * To use, go to IAM User, create an access key and secret, then add to the request
