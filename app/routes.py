from app import app

from flask import render_template, flash, redirect, url_for, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    return render_template('about_us.html', title='About Us')


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

