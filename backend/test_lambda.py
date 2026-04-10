import json
from unittest.mock import patch
from lambda_function import lambda_handler


#TEST GET
@patch("lambda_function.table")
def test_lambda_get_returns_200(mock_table):
    mock_table.get_item.return_value = {
        "Item": {"views": 1}
    }

    event = {
        "requestContext": {
            "http": {
                "method": "GET"
            }
        }
    }

    response = lambda_handler(event, None)

    assert response["statusCode"] == 200


@patch("lambda_function.table")
def test_lambda_get_returns_views_key(mock_table):
    mock_table.get_item.return_value = {
        "Item": {"views": 1}
    }

    event = {
        "requestContext": {
            "http": {
                "method": "GET"
            }
        }
    }

    response = lambda_handler(event, None)
    body = json.loads(response["body"])

    assert "views" in body


@patch("lambda_function.table")
def test_lambda_get_views_is_integer(mock_table):
    mock_table.get_item.return_value = {
        "Item": {"views": 1}
    }

    event = {
        "requestContext": {
            "http": {
                "method": "GET"
            }
        }
    }

    response = lambda_handler(event, None)
    body = json.loads(response["body"])

    assert isinstance(body["views"], int)


#TEST POST 
@patch("lambda_function.table")
@patch("lambda_function.cloudwatch")
def test_lambda_post_increments(mock_cloudwatch, mock_table):
    mock_table.update_item.return_value = {
        "Attributes": {"views": 2}
    }

    event = {
        "requestContext": {
            "http": {
                "method": "POST"
            }
        }
    }

    response = lambda_handler(event, None)
    body = json.loads(response["body"])

    assert response["statusCode"] == 200
    assert body["views"] == 2
