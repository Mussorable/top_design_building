import logging

from app import app
from app.logic.map import generate_map

from flask import render_template, flash, redirect, url_for, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    coordinates = [51.215950, 18.573541]
    folium_map = None

    try:
        folium_map = generate_map(coordinates)
    except ValueError:
        flash('Invalid coordinates provided.')
    except Exception as e:
        logging.error(f'Error generating map: {e}', exc_info=True)
        flash('Something went wrong while generating the map.')

    return render_template('about_us.html', title='About Us', map=folium_map)


@app.route('/services')
def services():
    return render_template('services.html', title='Services')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/realisations')
def realisations():
    return render_template('realisations.html', title='Realisations')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html', title='Reviews')
