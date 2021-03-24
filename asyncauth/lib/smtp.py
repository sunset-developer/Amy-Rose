from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from aiosmtplib import send
from asyncauth.core.config import config


async def send_email(to, subj, msg, text_type="plain"):
    """
    Sends an email using SMTP.

    :param to: To email.
    :param subj: Email subject.
    :param msg: Email message.
    :param text_type: Can be html or plain.
    """
    message = MIMEMultipart("alternative")
    message["From"] = config['SMTP']['from']
    message["To"] = to
    message["Subject"] = subj
    mime_text = MIMEText(msg, text_type, "utf-8")
    message.attach(mime_text)
    await send(
        message,
        hostname=config['SMTP']['host'],
        port=int(config['SMTP']['port']),
        username=config['SMTP']['username'],
        password=config['SMTP']['password'],
        use_tls=config['SMTP']['tls'] == 'true',
        start_tls=config['SMTP']['start_tls'] == 'true'
    )
