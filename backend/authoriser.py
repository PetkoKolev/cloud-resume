def lambda_handler(event, context):
    try:
        headers = event.get("headers", {})
        token = headers.get("authorization")

        if token == "my-secret-token":
            return {
                "isAuthorized": True
            }
        else:
            return {
                "isAuthorized": False
            }

    except Exception as e:
        print(f"Authorizer error: {str(e)}")

        return {
            "isAuthorized": False
        }
