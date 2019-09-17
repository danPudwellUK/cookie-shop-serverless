import unittest
from unittest.mock import MagicMock, patch
from src import orders_stream
from decimal import Decimal


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

        orders_stream.handler(event, None)

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

        orders_stream.handler(event, None)