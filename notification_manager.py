from twilio.rest import Client
import os

TWILIO_SID = "AC5c9d54bcdf1f1858921a5131a2d4a64d"
TWILIO_TOKEN = os.environ['TW_TOKEN']
TWILIO_VIRTUAL_NUMBER = "12398936307"
TWILIO_VERIFIED_NUMBER = os.environ['MY_NUMBER']


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)