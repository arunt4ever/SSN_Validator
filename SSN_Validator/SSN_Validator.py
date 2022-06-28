import json


def lambda_handler(event, context):
    responseMsg = ''
    responseCode = 200
    if 'callerSSN' in event['Details']['ContactData']['Attributes']:
        ssn = event['Details']['ContactData']['Attributes']['callerSSN']
        ssn_length = len(ssn)
        if not ssn.isnumeric():
            responseCode = '400'
            responseMsg = 'SSN is AlphaNumeric! only 9-digit numeric is accepted'
        elif ssn_length > 9:
            responseCode = '400'
            responseMsg = 'SSN is longer than accepted 9 Digit'
        elif ssn_length < 9:
            responseCode = '400'
            responseMsg = 'SSN is shorter than accepted 9 Digit'
        else:
            responseCode = '200'
            responseMsg = 'SSN is Valid'
    else:
        responseCode = '400'
        responseMsg = 'Missing Caller SSN Value'
    print(responseMsg)


    return {
        'statusCode': responseCode,
        'body': responseMsg
    }


if __name__ == '__main__':
    event = open("ConnectEvent.json", "r")
    j = json.loads(event.read())
    response = lambda_handler(j, "")
    print(response)
