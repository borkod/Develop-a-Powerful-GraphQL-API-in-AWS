import json
import boto3

def lambda_handler(event, context):
    hotel_id = event['arguments']['id']
    client = boto3.client('dynamodb')
    response = client.get_item(
        TableName='liveProject-Hotels',
        Key={
        'id': {
            'S': hotel_id
            }
        },
        ConsistentRead=False,
        ReturnConsumedCapacity='NONE',
    )
    
    hotel = {
      "id": hotel_id,
      "cidy": response['Item']['city']['S'],
      "short_description": response['Item']['short_description']['S'],
      "average": response['Item']['average']['N'],
      "number_of_votes": response['Item']['number_of_votes']['N'],
      "long_description": response['Item']['long_description']['S'],
      "hotel_name": response['Item']['hotel_name']['S']
    }
    print(hotel)
    return {
        'statusCode': 200,
        'body': json.dumps(hotel)
    }
