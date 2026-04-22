terraform {
  backend "s3" {
    bucket = "petko-terraform-state"
    key    = "cloud-resume/terraform.tfstate"
    region = "eu-west-2"
  }
}

provider "aws" {
  region = "eu-west-2"
}

resource "aws_dynamodb_table" "resume_table" {
  name         = "ResumeViewCount"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

resource "aws_iam_role" "lambda_role" {
  name = "resume_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_dynamodb" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess"
}

resource "aws_iam_role_policy_attachment" "lambda_basic" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "resume_lambda" {
  function_name = "resume-counter"

  filename         = "../backend/lambda.zip"
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.11"
  role             = aws_iam_role.lambda_role.arn

  source_code_hash = filebase64sha256("../backend/lambda.zip")
}

resource "aws_lambda_function" "authoriser_lambda" {
  function_name = "resume-authoriser"
  role          = aws_iam_role.lambda_role.arn
  handler       = "authoriser.lambda_handler"
  runtime       = "python3.11"

  filename         = "../backend/lambda.zip"
  source_code_hash = filebase64sha256("../backend/lambda.zip")
}

resource "aws_lambda_permission" "api_gw" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.resume_lambda.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_apigatewayv2_api.resume_api.execution_arn}/*/*"
}

resource "aws_apigatewayv2_api" "resume_api" {
  name          = "resume-counter-api"
  protocol_type = "HTTP"

  cors_configuration {
    allow_origins = ["https://petkokolev-cloud.com",
    "https://www.petkokolev-cloud.com"]
    allow_methods = ["GET", "POST", "OPTIONS"]
    allow_headers = ["*"]
  }
}

resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id                 = aws_apigatewayv2_api.resume_api.id
  integration_type       = "AWS_PROXY"
  integration_uri        = aws_lambda_function.resume_lambda.invoke_arn
  integration_method     = "POST"
  payload_format_version = "2.0"
}

resource "aws_apigatewayv2_route" "get_views" {
  api_id    = aws_apigatewayv2_api.resume_api.id
  route_key = "GET /views"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

resource "aws_apigatewayv2_stage" "prod" {
  api_id      = aws_apigatewayv2_api.resume_api.id
  name        = "prod"
  auto_deploy = true

  lifecycle {
    ignore_changes = all
  }
}

output "api_url" {
  value = aws_apigatewayv2_stage.prod.invoke_url
}
