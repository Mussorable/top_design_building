from flask import render_template
from flask_mail import Message
from app import app, mail

from threading import Thread


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body

    Thread(target=send_async_email, args=(app, msg)).start()


def send_contact_confirmation(user):
    send_mail(
        '[Top Design] Contact Form Confirmation',
        sender=app.config['ADMINS'],
        recipients=[user.email],
        text_body=render_template('email/form_confirmation.txt',
                                  user=user),
        html_body=render_template('email/form_confirmation.html',
                                  user=user)
    )
