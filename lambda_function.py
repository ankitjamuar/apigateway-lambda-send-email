import boto3
from botocore.exceptions import ClientError

# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "us-east-1"

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)


def lambda_handler(event, context):
    # Try to send the email.
    try:
        SENDER = event.get("sender",None) 
        RECIPIENT = event.get("recipient",None)
        SUBJECT = event.get("subject",None) 
        BODY_TEXT = event.get("body_text",None) 
        BODY_HTML = event.get("body_html",None) 
        CC = event.get("cc",None)
        
        TO_CC_BCC = {}
        if RECIPIENT is not None:
            TO_CC_BCC["ToAddresses"] = RECIPIENT.split(",")
        
        if CC is not None:
            TO_CC_BCC["CcAddresses"] = CC.split(",")
       
        #Provide the contents of the email.
        response = client.send_email(
            Destination=TO_CC_BCC,
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        return { "success": False, "message": e.response['Error']['Message']}
    else:
        return { "success": True, "message": "Email sent!", "message_id": response['ResponseMetadata']['RequestId'] }
