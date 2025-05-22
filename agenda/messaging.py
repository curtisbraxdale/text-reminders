from twilio.rest import Client
from datetime import date
import os

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE_NUMBER")
personal_phone = os.getenv("PERSONAL_NUMBER")

today = date.today()

def send_agenda_text(agenda):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    client = Client(account_sid, auth_token)
    if today.weekday() == 0:
        message_body = agenda.create_weekly_agenda()
    else:
        message_body = agenda.create_daily_agenda()
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone,
        to=personal_phone,
    )

    print(message.body)
