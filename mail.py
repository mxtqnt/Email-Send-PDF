import os
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apikey import PASSWORD, RECIVER, SENDER
from datetime import datetime

def enviar():
    class SendEmail:
        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        sender_email = SENDER
        receiver_email = RECIVER
        password = PASSWORD

        def __init__(self, subject, body):
            self.context = ssl.create_default_context()
            self.message = MIMEMultipart()
            self.message["From"] = self.sender_email
            self.message["To"] = self.receiver_email
            self.message["Subject"] = subject
            self.message.attach(MIMEText(body, "plain"))

        def add_attachment(self, path):
            for p in os.listdir(path):
                file_path = os.path.join(path, p)
                with open(file_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename= {p}")
                self.message.attach(part)

        def send(self):
            try:
                with smtplib.SMTP(self.smtp_server, self.port) as server:
                    server.ehlo()
                    server.starttls(context=self.context)
                    server.ehlo()
                    server.login(self.sender_email, self.password)
                    server.sendmail(self.sender_email, self.receiver_email, self.message.as_string())
            except Exception as e:
                print(e)

    # Exemplo de uso:
    subject = "Reletório de produção"
    body = "A seguir o relatório de produção dia " + str(datetime.now())[0:10]
    email = SendEmail(subject, body)
    email.add_attachment('anexos')
    email.send()