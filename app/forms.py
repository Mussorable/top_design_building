from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp


class ContactForm(FlaskForm):
    name = StringField('Your name', validators=[DataRequired()])
    email = EmailField('Your email', validators=[DataRequired(), Email()])
    phone_number = StringField('Your phone number', validators=[
        DataRequired(),
        Regexp(r'^\+?1?\d{9,15}$', message="Invalid phone number format."),
        Length(min=10, max=15, message="Phone number must be between 10 and 15 digits.")
    ])
    message = TextAreaField('Your message', validators=[DataRequired()])
    submit = SubmitField('Contact Us')


class EmailForm(FlaskForm):
    email = EmailField('For any questions, offers or comments please fill out the following form.', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')