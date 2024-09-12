import base64

from flask import render_template
from flask_mail import Message
from app import app, mail

from threading import Thread


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(subject, sender, recipients, text_body, html_body):
    with app.open_resource("static/images/logo.png", "rb") as img_file:
        logo_base64 = base64.b64encode(img_file.read()).decode("utf-8")

    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body

    html_body = html_body.replace('{{ log_base64 }}', logo_base64)
    msg.html = html_body

    Thread(target=send_async_email, args=(app, msg)).start()


def send_contact_confirmation(user, user_message):
    send_mail(
        '[Top Design] Contact Form Confirmation',
        sender=app.config['ADMINS'],
        recipients=[user.email],
        text_body=render_template('email/form_confirmation.txt',
                                  user=user, user_message=user_message),
        html_body=render_template('email/form_confirmation.html',
                                  user=user, user_message=user_message)
    )


def send_email_confirmation(email_record):
    send_mail(
        '[Top Design] Email Confirmation - Thank You for Providing Your Email!',
        sender=app.config['ADMINS'],
        recipients=[email_record.email],
        text_body=render_template('email/email_confirmation.txt', email_record=email_record),
        html_body=render_template('email/email_confirmation.html', email_record=email_record)
    )
