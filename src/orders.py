import boto3
import json
import os
import uuid
from http import HTTPStatus
from aws_dynamodb_parser import parse


ORDERS_DYNAMO_TABLE = os.environ.get("ORDERS_TABLE_NAME")
COOKIES_DYNAMO_TABLE = os.environ.get("COOKIES_TABLE_NAME")


def post_handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb").Table(ORDERS_DYNAMO_TABLE)
        
        event_data = json.loads(event['body'])
        
        data = {
            "id": str(uuid.uuid4()),
            "cookie_id": event_data['cookie_id'],
            "quantity": event_data['quantity']
        }

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

def stream_handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb").Table(COOKIES_DYNAMO_TABLE)

        for record in event['Records']:
            entry = parse(record["dynamodb"]["NewImage"])
            cookie_item = dynamodb.get_item(Key={"id": entry['cookie_id']})
            cookie_item["Item"]['quantity'] = cookie_item["Item"]['quantity'] - entry['quantity']
            dynamodb.put_item(Item=cookie_item)

    except Exception as e:
        print("There was a problem: {}".format(e))
