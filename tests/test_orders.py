import unittest
from unittest.mock import MagicMock, patch
import uuid
from src import orders
from http import HTTPStatus
import json

class OrderPostTests(unittest.TestCase):

    @patch("boto3.resource")
    def test_put_order_successfully(self, mock_dynamo):

        test_order = {
            "id": str(uuid.uuid4()),
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