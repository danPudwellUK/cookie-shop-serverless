import boto3
import json
import os
import uuid
from http import HTTPStatus


ORDERS_DYNAMO_TABLE = os.environ.get("ORDERS_TABLE_NAME")


def post_handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb").Table(ORDERS_DYNAMO_TABLE)
        print("******************")
        print(event)
        event_data = json.loads(event['body'])
        print("******************")
        print(event_data)
        data = {
            "id": str(uuid.uuid4()),
            "cookie_id": event_data['id'],
            "quantity": event_data['quantity']
        }
        print("******************")
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
