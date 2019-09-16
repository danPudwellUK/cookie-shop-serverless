import boto3
import json
import os
import uuid
from http import HTTPStatus


COOKIES_DYNAMO_TABLE = os.environ.get("COOKIES_TABLE_NAME")


def get_handler(event, context):
    dynamodb = boto3.resource("dynamodb").Table(COOKIES_DYNAMO_TABLE)
    cookies = dynamodb.scan().get("Items", [])

    return {
        "statusCode": HTTPStatus.OK,
        "body": json.dumps(cookies)
    }


def post_handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb").Table(COOKIES_DYNAMO_TABLE)
        event_data = json.loads(event['body'])
        data = {
            "id": str(uuid.uuid4()),
            "name": event_data['name'],
            "description": event_data['description'],
            "quantity": event_data['quantity']
        }
        print(data)
        dynamodb.put_item(Item=data)

        return {
            "statusCode": HTTPStatus.CREATED,
            "body": json.dumps(data)
        }
    except Exception as e:
        print("There was a problem: {}".format(e))
        return {
            "statusCode": HTTPStatus.BAD_REQUEST
        }
