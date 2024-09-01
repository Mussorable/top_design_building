import logging

from app import app
from app.logic.map import generate_map
from app.forms import ContactForm

from flask import render_template, flash, redirect, url_for, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', active_page=request.endpoint)


@app.route('/about')
def about():
    folium_map = generate_map()

    return render_template('about_us.html', title='About Us', map=folium_map, active_page=request.endpoint)


@app.route('/services')
def services():
    return render_template('services.html', title='Services', active_page=request.endpoint)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        flash('Your message is sent.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', title='Contact', form=contact_form, active_page=request.endpoint)


@app.route('/realisations')
def realisations():
    return render_template('realisations.html', title='Realisations', active_page=request.endpoint)


@app.route('/reviews')
def reviews():
    return render_template('reviews.html', title='Reviews', active_page=request.endpoint)


@app.route('/policy')
def policy():
    return render_template('policy.html', title='Privacy Policy', active_page=request.endpoint)
