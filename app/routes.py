import logging
from crypt import methods

from wtforms.validators import email

from app import app, db
from app.email import send_contact_confirmation, send_email_confirmation
from app.logic.map import generate_map
from app.forms import ContactForm, EmailForm
from app.models import User, ContactEmail

from flask import render_template, flash, redirect, url_for, request


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        title='Top Design',
        active_page=request.endpoint,
        header_image='new_apartment',
        is_under_header_caption=True
    )


@app.route('/about')
def about():
    folium_map = generate_map()

    return render_template(
        'about_us.html',
        title='About Us',
        map=folium_map,
        active_page=request.endpoint,
        header_image='background_team'
    )


@app.route('/services')
def services():
    return render_template(
        'services.html',
        title='Services',
        active_page=request.endpoint,
        header_image='services_header'
    )


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        user_customer = User(
            full_name=contact_form.name.data,
            email=contact_form.email.data,
            phone_number=contact_form.phone_number.data,
            text_message=contact_form.message.data,
        )

        db.session.add(user_customer)
        db.session.commit()

        if user_customer:
            send_contact_confirmation(user_customer)

        flash('Your message is sent.', 'success')
        return redirect(url_for('index'))
    elif request.method == 'POST':
        flash('Please, fill out the form correctly.', 'danger')
    return render_template(
        'contact.html',
        title='Contact',
        form=contact_form,
        active_page=request.endpoint,
        header_image='old-to-new'
    )


@app.route('/realisations')
def realisations():
    return render_template(
        'realisations.html',
        title='Realisations',
        active_page=request.endpoint,
        header_image='calm-apartment'
    )


@app.route('/realisations/<type_of_room>')
def realisations_type(type_of_room):
    title_list = type_of_room.split('-')
    capitalized_list = []
    for word in title_list:
        capitalized_list.append(word.capitalize())
    title = ' '.join(capitalized_list)
    title_url = title.replace(' ', '-').lower()

    return render_template(
        'type-of-room.html',
        title=title,
        active_page=request.endpoint,
        header_image=title_url
    )


@app.route('/reviews')
def reviews():
    return render_template(
        'reviews.html',
        title='Reviews',
        active_page=request.endpoint,
        header_image='abstract_wall'
    )


@app.route('/policy')
def policy():
    return render_template(
        'policy.html',
        title='Privacy Policy',
        active_page=request.endpoint,
        header_image='calm-apartment'
    )


@app.route('/submit_email', methods=['POST'])
def submit_email():
    email_form = EmailForm()
    if email_form.validate_on_submit():
        email_record = ContactEmail(email=email_form.email.data)

        db.session.add(email_record)
        db.session.commit()

        if email_form:
            send_email_confirmation(email_record)

        flash('Your email has been successfully sent and saved. '
              'We appreciate your interest and will get back to you shortly.')
        redirect(url_for('index'))
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        '404.html',
        title='Top Design (404)',
        header_image='new_apartment',
        is_under_header_caption=True
    ), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template(
        '500.html',
        title='Top Design (500)',
        header_image='new_apartment',
        is_under_header_caption=True
    ), 500


@app.context_processor
def utility_processor():
    email_form = EmailForm()

    return dict(email_form=email_form)
