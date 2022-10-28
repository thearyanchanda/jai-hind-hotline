from flask import Flask
import os
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("Welcome to the Jai Hind Hotline. Long live India.", voice='alice')

    resp.play("https://replit.com/@MistaRen476/jai-hind-hotline#Jana%20Gana%20Mana%20V2.mp3")

    return str(resp)

app.run(debug=True)