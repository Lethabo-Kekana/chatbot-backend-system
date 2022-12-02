import json

from common_function import delete_intent


def lambda_handler(event, context):
    path_parameters = event.get("pathParameters") or dict()

    intent_id = path_parameters.get('intent_id')

    return {
        "statusCode": 200,
        "headers": {
            "content-type": "application/json",
            "Access-Control-Allow-Origin": '*'
        },
        "body": json.dumps({
            "data": delete_intent(intent_id)
        }),
    }
