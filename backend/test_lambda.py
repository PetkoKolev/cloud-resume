import json
from lambda_function import lambda_handler


def test_lambda_returns_200():
    """
    Test 1: Lambda should return HTTP 200 - Successful request code 
    """
    event = {"httpMethod": "GET"}

    response = lambda_handler(event, None)

    assert response["statusCode"] == 200


def test_lambda_returns_views_key():
    """
    Test 2: Response contains 'views' to match frontend design
    """
    event = {"httpMethod": "GET"}

    response = lambda_handler(event, None)
    body = json.loads(response["body"])

    assert "views" in body


def test_lambda_views_is_integer():
    """
    Test 3: Check views is a number not string
    """
    event = {"httpMethod": "GET"}

    response = lambda_handler(event, None)
    body = json.loads(response["body"])

    assert isinstance(body["views"], int)