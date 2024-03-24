import smtplib


class Mailer:

    def __init__(self, host, email_from, pw, port=587):
        self.host = host
        self.email_from = email_from
        self.password = pw
        self.port = port

    def validate(self):
        if (len(self.host) == 0 or len(self.email_from) == 0 or
                len(self.password) == 0 or self.port <= 0):
            return False
        return True

    def send(self, email_to, subject, content):
        if len(email_to) == 0 or ~self.validate():
            print("Invalid configuration.")
            print(f"Unable to send:\n{subject}\n\n{content}")
            return

        with smtplib.SMTP(self.host, self.port) as connection:
            connection.starttls()
            connection.login(user=self.email_from, password=self.password)
            connection.sendmail(from_addr=self.email_from, to_addrs=email_to,
                                msg=f"Subject:{subject}\n\n{content}")
