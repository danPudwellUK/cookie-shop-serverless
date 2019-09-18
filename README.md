# cookie-shop-serverless

This is an example project for Serverless in AWS
We will be using SAM (https://github.com/awslabs/serverless-application-model)
Most services will be using the free tier so costs should be very minimal.

Prerequisites:
1) Signup for an AWS account

2) Fork this project into your GitHub account

3) Python 3.7


Activity:
1) Run the setup-template.yaml in AWS Cloudformation

2) Create a CodeBuild project

3) Run the build

4) Explore the project and created resources in Dynamo, Lambda, API Gateway

4) Add a stream to our Orders DynamoDB
When an order is placed it will now update the quantity of cookies left

5) Add authentication
The orders endpoint is now protected by IAM (AWS sigv4)