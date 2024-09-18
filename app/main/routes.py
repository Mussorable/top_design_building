from flask import render_template, current_app, flash, redirect, url_for, request
from flask_babel import _

from app.email import send_contact_confirmation, send_administrator_notification, send_email_confirmation
from app.logic.gallery_images import get_gallery
from app.main import bp
from app.main.forms import ContactForm, EmailForm
from app.logic.map import generate_map
from app.models import User, ContactEmail, Message
from app import db


@bp.route('/')
@bp.route('/index')
def index():
    home_name = _('Home')
    footer_question = _("Got a Question? Share your email and We'll write you")
    return render_template(
        'index.html',
        title=current_app.config['TITLE'],
        header_image='new_apartment',
        active_page=request.endpoint,
        is_under_header_caption=True
    )


@bp.route('/about')
def about():
    folium_map = generate_map()

    return render_template(
        'about_us.html',
        title=_('About Us'),
        website_title=current_app.config['TITLE'],
        map=folium_map,
        active_page=request.endpoint,
        header_image='example_rw_3'
    )


@bp.route('/services')
def services():
    return render_template(
        'services.html',
        title=_('Services'),
        website_title=current_app.config['TITLE'],
        active_page=request.endpoint,
        header_image='services_header'
    )


@bp.route('/realisations')
def realisations():
    return render_template(
        'realisations.html',
        title=_('Realisations'),
        website_title=current_app.config['TITLE'],
        active_page=request.endpoint,
        header_image='calm-apartment'
    )


@bp.route('/realisations/<type_of_room>')
def realisations_type(type_of_room):
    title_list = type_of_room.split('-')
    gallery_type = request.args.get('gallery_type')
    capitalized_list = []
    for word in title_list:
        capitalized_list.append(word.capitalize())
    title = ' '.join(capitalized_list)
    title_url = title.replace(' ', '-').lower()

    gallery = get_gallery()
    room_images = gallery.get(title_url)
    if room_images is None:
        flash(
            _("Sorry, the room type you're looking for doesn't exist. Please select a type that exists from the options below."),
            'danger')
        return redirect(url_for('main.realisations'))

    return render_template(
        'type-of-room.html',
        title=title,
        gallery_type=gallery_type,
        website_title=current_app.config['TITLE'],
        active_page=request.endpoint,
        header_image=title_url,
        room_images=room_images,
        images_length=len(room_images),
        images_row=len(room_images) // 2 + len(room_images) % 2
    )


@bp.route('/reviews')
def reviews():
    return render_template(
        'reviews.html',
        title=_('Reviews'),
        website_title=current_app.config['TITLE'],
        active_page=request.endpoint,
        header_image='abstract_wall'
    )


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        email = contact_form.email.data
        full_name = contact_form.name.data
        phone_number = contact_form.phone_number.data
        text_message = contact_form.message.data

        if phone_number.startswith('+48 '):
            phone_number = phone_number.replace('+48 ', '')

        user_customer = User.query.filter_by(email=email, phone_number=phone_number).first()
        email_record = ContactEmail.query.filter_by(email=email).first()
        if not user_customer:
            user_customer = User(
                full_name=full_name,
                email=email,
                phone_number=phone_number,
            )
            db.session.add(user_customer)
            db.session.flush()

        if not email_record:
            email_record = ContactEmail(email=email)
            db.session.add(email_record)

        new_message = Message(text_message=text_message, user_id=user_customer.id)
        db.session.add(new_message)

        db.session.commit()

        if user_customer:
            send_contact_confirmation(user_customer, new_message)
            send_administrator_notification(user_customer, new_message)

        flash(_('Thank you! Your message has been successfully sent. We’ll get back to you shortly.'), 'success')
        return redirect(url_for('main.index'))
    elif request.method == 'POST':
        flash(_('Oops! Something went wrong. Please try again or contact us directly.'), 'danger')
    return render_template(
        'contact.html',
        title=_('Contact'),
        website_title=current_app.config['TITLE'],
        form=contact_form,
        active_page=request.endpoint,
        header_image='old-to-new',
        contact_email=current_app.config['CONTACT_EMAIL']
    )


@bp.route('/policy')
def policy():
    website_title = current_app.config['TITLE']
    contact_email = current_app.config['CONTACT_EMAIL']

    return render_template(
        'policy.html',
        title=_('Privacy Policy'),
        website_title=website_title,
        active_page=request.endpoint,
        header_image='calm-apartment',
        contact_email=contact_email
    )


@bp.route('/submit_email', methods=['POST'])
def submit_email():
    email_form = EmailForm()
    if email_form.validate_on_submit():
        email_address = email_form.email.data
        email_record = ContactEmail.query.filter_by(email=email_address).first()

        if not email_record:
            email_record = ContactEmail(email=email_address)
            db.session.add(email_record)
            db.session.commit()

        if email_record:
            send_email_confirmation(email_record)
        else:
            flash(_('Oops! Something went wrong. Please try again or contact us directly.'), 'danger')
            return redirect(url_for('main.realisations'))

        flash(_('Your email has been successfully sent and saved. '
                'We appreciate your interest and will get back to you shortly.'))
        redirect(url_for('main.index'))
    return redirect(url_for('main.index'))
