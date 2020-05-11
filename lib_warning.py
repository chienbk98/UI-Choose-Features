import smtplib
from twilio.rest import Client
from playsound import playsound

gmail_user = 'yoonalearning@gmail.com'
gmail_password = 'yeuyoona98'

sent_from = gmail_user
to = ['yoonachien@gmail.com']
subject = 'Warning Message'
body = 'Someone are entering the restricted area'

message = 'Subject: {}\n\n{}'.format(subject, body)

def sendemail(message):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(gmail_user, gmail_password)
  server.sendmail(sent_from, to, message)
  server.quit()


def sendSMS():
  account_sid = 'ACb0f57f89aed94e673c4d2ff094c53ff4'
  auth_token = '4804e39f1e6519ebd675dd73af2e5b2b'
  client = Client(account_sid, auth_token)
  message = client.messages.create(
                                from_='+12057820497',
                                body=body,
                                to='+84812749258'
                            )
  print(message.sid)


def makeCall():
  account_sid = 'ACb0f57f89aed94e673c4d2ff094c53ff4'
  auth_token = '4804e39f1e6519ebd675dd73af2e5b2b'
  client = Client(account_sid, auth_token)
  call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+84812749258',
                        from_='+12057820497'
                    )

  print(call.sid)


def soundWarning():
  playsound('warning.mp3')
