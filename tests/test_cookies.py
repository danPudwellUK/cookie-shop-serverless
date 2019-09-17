import unittest
from unittest.mock import MagicMock, patch
from src import cookies
from http import HTTPStatus
import json
from decimal import Decimal


class CookieGetTests(unittest.TestCase):

    TEST_COOKIE = {
        "id": "uuid",
        "name": "Chocolate Chip",
        "description": "It's very good",
        "quantity": Decimal('10')
    }
    @patch("boto3.resource")
    def test_get_cookies_successfully(self, mock_dynamo):

        mock_table = MagicMock()
        mock_table.scan.return_value = {
            "Items": [self.TEST_COOKIE.copy()]
        }
        mock_dynamo.return_value.Table.return_value = mock_table

        response = cookies.get_handler(None, None)
        self.assertEqual(response["statusCode"], HTTPStatus.OK)


class CookiePostTests(unittest.TestCase):

    @patch("boto3.resource")
    def test_put_cookies_successfully(self, mock_dynamo):

        test_cookie = {
            "name": "Chocolate Chip",
            "description": "It's very good",
            "quantity": 10
        }
        event = {
            "body": json.dumps(test_cookie)
        }

        mock_table = MagicMock()
        mock_table.put_item.return_value = {}
        mock_dynamo.return_value.Table.return_value = mock_table

        response = cookies.post_handler(event, None)
        self.assertEqual(response["statusCode"], HTTPStatus.CREATED)

    @patch("boto3.resource")
    def test_put_cookies_unsuccessfully(self, mock_dynamo):

        test_cookie = {}
        event = {
            "body": json.dumps(test_cookie)
        }

        mock_table = MagicMock()
        mock_table.put_item.return_value = {}
        mock_dynamo.return_value.Table.return_value = mock_table

        response = cookies.post_handler(event, None)
        self.assertEqual(response["statusCode"], HTTPStatus.BAD_REQUEST)