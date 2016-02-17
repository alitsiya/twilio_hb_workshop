# https://www.twilio.com/docs/quickstart/python/rest/call-request
# makes an outgoing call

# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient


# Get these credentials from http://twilio.com/user/account
account_sid = "ACc7c2835d0a12a91ebcdb11b305c11688"
auth_token = "5c776c7ec25bc14dc8a2f2d6d46e55d3"
client = TwilioRestClient(account_sid, auth_token)
 
# Make the call
call = client.calls.create(to="+14252143104",  # Any phone number
                           from_="+14255288154", # Must be a valid Twilio number
                           # url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
                            url="http://twimlbin.com/external/870acf0f7235ae3c")
print call.sid