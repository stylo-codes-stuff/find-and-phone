

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

client = Client(account_sid, auth_token)

phone_number = client.lookups \
                     .v2 \
                     .phone_numbers('+12149064027') \
                     .fetch(fields='line_type_intelligence')

print(phone_number.line_type_intelligence)