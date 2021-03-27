import os
from twilio.rest import Client

account_sid = "AC28999e1381dad41361921db3aec94088"
auth_token = "630e481b1a395878f3bc3a45445d96aa"

client = Client(account_sid,auth_token)

client.messages.create(
    to="+306949265126",
    from_="+14089121471",
    body= "Testing messaging with python from my computer"
)