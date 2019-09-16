import boto3
import json
import os
import uuid
from http import HTTPStatus


ORDERS_DYNAMO_TABLE = os.environ.get("ORDERS_TABLE_NAME")


def post_handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb").Table(ORDERS_DYNAMO_TABLE)
        event_data = json.loads(event['body'])
        data = {
            "id": str(uuid.uuid4()),
            "cookie_id": event_data['id'],
            "quantity": event_data['quantity']
        }
        dynamodb.put_item(Item=data)

        return {
            "statusCode": HTTPStatus.CREATED,
            "body": json.dumps(data)
        }
    except:
        print("There was a problem")
        return {
            "statusCode": HTTPStatus.BAD_REQUEST
        }
