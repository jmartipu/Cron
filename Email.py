import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import Settings
# set up the SMTP server


class Email:
    @staticmethod
    def send_email(name, tittle, email):
        s = smtplib.SMTP(host='smtp.office365.com', port=587)
        s.starttls()
        s.login(Settings.EMAIL_ADDRESS, Settings.EMAIL_PASSWORD)
        msg = MIMEMultipart()  # create a message
        message = "Gracias por usar supervoices,  " + name + "\n Su archivo " + tittle +  " ya fue cargado"

        msg['From'] = Settings.EMAIL_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Supervoices! - Carga Exitosa"
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg
        s.quit()
