import json
from unittest.mock import patch
from lambda_function import lambda_handler


@patch("lambda_function.table")
def test_lambda_returns_200(mock_table):
    mock_table.update_item.return_value = {
        "Attributes": {"views": 1}
    }

    event = {"httpMethod": "GET"}
    response = lambda_handler(event, None)

    assert response["statusCode"] == 200


@patch("lambda_function.table")
def test_lambda_returns_views_key(mock_table):
    mock_table.update_item.return_value = {
        "Attributes": {"views": 1}
    }

    event = {"httpMethod": "GET"}
    response = lambda_handler(event, None)

    body = json.loads(response["body"])

    assert "views" in body


@patch("lambda_function.table")
def test_lambda_views_is_integer(mock_table):
    mock_table.update_item.return_value = {
        "Attributes": {"views": 1}
    }

    event = {"httpMethod": "GET"}
    response = lambda_handler(event, None)

    body = json.loads(response["body"])

    assert isinstance(body["views"], int)
