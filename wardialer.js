// Download the helper library from https://www.twilio.com/docs/node/install
// Find your Account SID and Auth Token at twilio.com/console
// and set the environment variables. See http://twil.io/secure
const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

client.lookups.v2.phoneNumbers('+447772000001')
                 .fetch({fields: 'sim_swap,call_forwarding'})
                 .then(phone_number => console.log(phone_number.valid));