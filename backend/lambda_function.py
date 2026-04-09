import json
import boto3
from decimal import Decimal
import time

dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
table = dynamodb.Table('ResumeViewCount')

cloudwatch = boto3.client('cloudwatch', region_name='eu-west-2')

def lambda_handler(event, context):
    try:
        print(f"Request received: {json.dumps(event)}")

        response = table.update_item(
            Key={'id': 'counter'},
            UpdateExpression='ADD #v :inc',
            ExpressionAttributeNames={
                '#v': 'views'
            },
            ExpressionAttributeValues={
                ':inc': 1
            },
            ReturnValues='UPDATED_NEW'
        )

        views = int(response['Attributes']['views'])

        print(f"Updated view count: {views}")

        try:
            cloudwatch.put_metric_data(
                Namespace='ResumeApp',
                MetricData=[
                    {    
                        'MetricName': 'ViewCount',
                        'Value': 1,
                        'Unit': 'Count'
                    }
                ]
            )
        except Exception as e:
            print(f"CloudWatch error {e}")
        
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'views': views
            })
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")

        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': 'Internal Server Error'
            })
        }
