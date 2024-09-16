# Top Design Building

**Top Design Building** is a website for a small construction company specializing in interior finishing work for apartments, houses, offices, business premises, and other commercial spaces.

## Project Description

This project is built using Python and Flask and is designed to showcase the services of a construction company. The website provides clients with information about the company, its services, and completed projects.

## Technologies

The project is based on the following technologies:
- **Backend**: Python 3, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLAlchemy

## Requirements

To run the project, you need to install the following dependencies:
- see **requirements.txt**

**deploy requirements**
aiosmtpd==1.4.4.post2
alembic==1.13.2
argcomplete==3.3.0
atpublic==3.1.1
attrs==23.2.0
babel==2.16.0
Beaker==1.12.1
beautifulsoup4==4.12.3
blinker==1.8.2
boto3==1.35.12
botocore==1.35.12
branca==0.7.2
cffi==1.16.0
charset-normalizer==3.3.2
click==8.1.7
cryptography==41.0.7
cssmin==0.2.0
distro==1.9.0
email_validator==2.2.0
file-magic==0.4.0
Flask==3.0.3
Flask-Assets==2.1.0
flask-babel==4.0.0
Flask-Login==0.6.3
Flask-Mail==0.10.0
Flask-Migrate==4.0.7
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.1
folium==0.17.0
greenlet==3.0.3
gunicorn==23.0.0
humanize==3.13.1
idna==3.7
iso639==0.1.4
xdg==6.0.0
pyxdg==0.28
itsdangerous==2.2.0
Jinja2==3.1.4
jmespath==1.0.1
jsmin==3.0.1
langtable==0.0.68
libsass==0.23.0
lxml==5.1.0
Mako==1.2.3
MarkupSafe==2.1.3
numpy==2.0.1
olefile==0.47
packaging==23.2
Paste==3.7.1
pexpect==4.9.0
pid==2.2.3
pillow==10.3.0
pip==24.2
ply==3.11
productmd==1.38
psycopg2-binary==2.9.9
ptyprocess==0.7.0
pycparser==2.20
pyenchant==3.2.2
pyOpenSSL==23.2.0
PySocks==1.7.1
python-dateutil==2.8.2
python-dotenv==1.0.1
pytz==2024.2
PyYAML==6.0.1
regex==2024.4.28
requests==2.31.0
s3transfer==0.10.2
setuptools==72.1.0
simpleline==1.9.0
six==1.16.0
soupsieve==2.5
SQLAlchemy==2.0.32
Tempita==0.5.2
typing_extensions==4.12.2
urllib3==1.26.19
webassets==2.0
Werkzeug==3.0.3
WTForms==3.1.2
xyzservices==2024.6.0

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/top_design_building.git
cd top_design_building
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file with settings for your environment (e.g., database configuration, mail server, etc.).
4. Run the database migrations:
```bash
flask db upgrade
```

## Usage
Once installed and running, the website will provide information about the company, its services, and a portfolio of completed projects. Users can contact the company via a contact form and explore the main service areas.

## Author
Oleh Diakov

## License
The project is free for use, except for files such as photos, videos, and client data, which cannot be used without explicit permission.