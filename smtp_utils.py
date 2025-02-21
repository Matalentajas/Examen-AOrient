import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

##Voy a cojer mis credenciales de email que tengo en un txt
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_EMAIL = "arturotest1305@gmail.com"
SMTP_PASSWORD = "awqm stxp mcoi dmms"

def saludo_email(email, username):
    try:
        msg = MIMEMultipart()
        msg["From"] = SMTP_EMAIL
        msg["To"] = email
        msg["Subject"] = "Correo de saludo"

        body = "Bienvenido {}, agradecemos tu confianza".format(username)
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, email, msg.as_string())
        server.quit()
    except Exception as e:
        print (e)

def send_reset_password(email, reset_url):
    try:
        msg = MIMEMultipart()
        msg["From"] = SMTP_EMAIL
        msg["To"] = email
        msg["Subject"] = "Correo de saludo"

        body = "Para poder recuperar la contraseña por favor accede al siguiente enlace: {}".format(reset_url)
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, email, msg.as_string())
        server.quit()
    except Exception as e:
        print (e)