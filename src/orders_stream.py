from aws_dynamodb_parser import parse
import boto3
import os


COOKIES_DYNAMO_TABLE = os.environ.get("COOKIES_TABLE_NAME")


def handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb").Table(COOKIES_DYNAMO_TABLE)

        for record in event['Records']:
            entry = parse(record["dynamodb"]["NewImage"])
            cookie_item = dynamodb.get_item(Key={"id": entry['cookie_id']})
            print("************")
            print(cookie_item)
            cookie_item["Item"]['quantity'] = cookie_item["Item"]['quantity'] - entry['quantity']
            print("************")
            print(cookie_item)
            dynamodb.put_item(Item=cookie_item)

    except Exception as e:
        print("There was a problem: {}".format(e))