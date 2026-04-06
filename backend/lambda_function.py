import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
table = dynamodb.Table('ResumeViewCount')

def lambda_handler(event, context):
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

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'views': int(response['Attributes']['views'])
        })
    }
