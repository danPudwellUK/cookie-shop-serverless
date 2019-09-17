import unittest
from unittest.mock import MagicMock, patch
from src import orders
from http import HTTPStatus
import json
from decimal import Decimal


class OrderPostTests(unittest.TestCase):

    @patch("boto3.resource")
    def test_put_order_successfully(self, mock_dynamo):

        test_order = {
            "cookie_id": "uuid",
            "quantity": 1
        }
        event = {
            "body": json.dumps(test_order)
        }

        mock_table = MagicMock()
        mock_table.put_item.return_value = {}
        mock_dynamo.return_value.Table.return_value = mock_table

        response = orders.post_handler(event, None)
        self.assertEqual(response["statusCode"], HTTPStatus.CREATED)

    @patch("boto3.resource")
    def test_put_orders_unsuccessfully(self, mock_dynamo):

        test_order= {}
        event = {
            "body": json.dumps(test_order)
        }

        mock_table = MagicMock()
        mock_table.put_item.return_value = {}
        mock_dynamo.return_value.Table.return_value = mock_table

        response = orders.post_handler(event, None)
        self.assertEqual(response["statusCode"], HTTPStatus.BAD_REQUEST)

class OrderStreamTests(unittest.TestCase):

    TEST_COOKIE = {
        "id": "uuid",
        "name": "Chocolate Chip",
        "description": "It's very good",
        "quantity": Decimal('10')
    }

    @patch("boto3.resource")
    def test_update_cookie_successfully(self, mock_dynamo):

        event = {
            "Records": [{
                "dynamodb": {
                    "NewImage": {
                        "cookie_id": {
                            "S": "uuid"
                        },
                        "quantity": {
                            "N": "1"
                        }
                    }
                }    
            }]
        }

        mock_table = MagicMock()
        mock_table.get_item.return_value = {
            "Item": self.TEST_COOKIE.copy()
        }
        mock_table.put_item.return_value = {}
        mock_dynamo.return_value.Table.return_value = mock_table

        orders.stream_handler(event, None)

    @patch("boto3.resource")
    def test_update_cookie_unsuccessfully(self, mock_dynamo):

        event = {
            "Records": [{
                "dynamodb": {
                    "NewImage": {
                        "cookie_id": {
                            "S": "uuid"
                        },
                        "quantity": {
                            "N": "1"
                        }
                    }
                }    
            }]
        }

        mock_table = MagicMock()
        mock_table.get_item.return_value = {}
        mock_table.put_item.return_value = {}
        mock_dynamo.return_value.Table.return_value = mock_table

        orders.stream_handler(event, None)
