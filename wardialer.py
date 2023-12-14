
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import time


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

client = Client(account_sid, auth_token)
start_number = 12034770000
with open("log.txt","w") as f:
    while True:
        phone_number = client.lookups \
                             .v2 \
                             .phone_numbers(start_number) \
                            .fetch(fields='country_code')
        print(phone_number.line_type_intelligence)
        f.write(str(phone_number.line_type_intelligence))
        print(start_number)
        start_number += 1
        
