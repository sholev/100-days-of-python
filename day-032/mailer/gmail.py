import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError


def send_mail(email_to, subject, body):
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', ["https://www.googleapis.com/auth/gmail.send"])

    creds = flow.run_local_server(port=0)

    service = build('gmail', 'v1', credentials=creds)

    message = MIMEText(body)
    message['to'] = email_to
    message['subject'] = subject
    body = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        messages = service.users().messages()
        message = messages.send(userId="me", body=body).execute()
        print(F'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occurred: {error}')
