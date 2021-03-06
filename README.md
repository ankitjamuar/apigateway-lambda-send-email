# Api Gateway Lambda Send Email
Serverless email sending capability using AWS Lambda &amp; API Gateway

# params
SENDER    = event.get("sender",None) 
RECIPIENT = event.get("recipient",None)
SUBJECT   = event.get("subject",None) 
BODY_TEXT = event.get("body_text",None) 
BODY_HTML = event.get("body_html",None) 
CC        = event.get("cc",None)

Params are self explanatory, RECIPIENT & CC can be a comma seperated list

The script starts with initializing SES client and then it gets all the params from LAMBDA event object. And finally, send email using the send_email function.

This Lambda function should be linked with API Gateway in order to make it accessible:

# Sample JSON:  
{"sender": "info@gmail.com","recipient": "xyz@gmail.com,abc@gmail.com","subject":"Multi Email","body_text": "This is textual body","body_html": "This is html Body","cc":"ankit@gmail.com"}

# SES Configuration
Befre SES is able to send email, the sending email address should be verified, which can be easily done from the console. Also initially the email sending service is in sandbox mode, so you need to raise a request to increase the limit using AWS Support.

# API Gateway
API gateway provide a way to ccreate public facing API, with an ability to make authenticated API using tokens. Based on the requirement you can create corresponding api(s). There are other fancy features like Throttling etc to help you secure your endpoint.
