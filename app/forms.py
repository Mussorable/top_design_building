from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l
from wtforms.fields.simple import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp


class ContactForm(FlaskForm):
    name = StringField(_l('Your name'), validators=[DataRequired()])
    email = EmailField(_l('Your email'), validators=[DataRequired(), Email()])
    phone_number = StringField(_l('Your phone number'), validators=[
        DataRequired(),
        Regexp(r'^\+?1?(\d{3}\s?){2,5}\d{3}$', message=_l("Invalid phone number format.")),
        Length(min=10, max=15, message=_l("Phone number must be between 10 and 15 digits."))
    ])
    message = TextAreaField(_l('Your message'), validators=[DataRequired()])
    submit = SubmitField(_l('Contact Us'))


class EmailForm(FlaskForm):
    email = EmailField(_l('For any questions, offers or comments please fill out the following form.'),
                       validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Submit'))
