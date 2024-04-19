import smtplib
from dotenv import dotenv_values
from email.mime.text import MIMEText

config = dotenv_values("../../.env")
EMAIL = config["GMAIL_USER"]


class Mailer:

    def __init__(self, host, email_from, pw, port=smtplib.SMTP_SSL_PORT):
        self.host = host
        self.email_from = email_from
        self.password = pw
        self.port = port

    def send(self, email_to, subject, content):
        msg = MIMEText(content)
        msg["From"] = self.email_from
        msg["To"] = email_to
        msg["Subject"] = subject
        with smtplib.SMTP_SSL(self.host, self.port) as connection:
            connection.login(user=self.email_from, password=self.password)
            connection.sendmail(from_addr=self.email_from, to_addrs=email_to,
                                msg=msg.as_string())


mailer = Mailer(config["ABV_SMTP"], config["ABV_USER"], config["ABV_PASS"])


def receive_mail(subject: str, content: str, email_to: str = EMAIL):
    mailer.send(email_to, subject, content)
