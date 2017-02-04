from email.mime.text import MIMEText
import smtplib


def send_email(name, email, message):
    from_email = 'hephaestusprogramming@gmail.com'
    from_password = '3783497.GGr'
    to_email = email

    subject = 'Glenn Rudge'
    message = "<h1>Hey there %s, </h1><br> Thanks for visiting my page. I'll be in contact with you as soon as possible! You can visit my GitHub <a href='https://github.com/IntoTheQCD'>here</a> " %name

    msg = MIMEText(message, 'html')

    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)