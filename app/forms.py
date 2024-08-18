from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class ContactForm(FlaskForm):
    name = StringField('Your name', validators=[DataRequired()])
    email = StringField('Your email', validators=[DataRequired(), Email()])
    phone_number = StringField('Your phone number', validators=[DataRequired()])
    message = StringField('Your message', validators=[DataRequired()])
    submit = SubmitField('Contact Us')
