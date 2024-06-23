import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('planets')

def lambda_handler(event, context):
    table.put_item(
        Item = {     #called as dictionary rather than objects
            'id': 'neptune',
            'temp': 'super cold'
        }
    )
    return {
        'statusCode' : 200,
        'body'  : 'Item added'
    }