import unittest

from app import create_app, db
from app.main.routes import contact
from app.models import User, ContactEmail, Message
from config import Config


class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # Get index page
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, f'Test failed: status code {response.status_code}')

    # Send contact form
    def test_contact_page(self):
        post_data = {
            'name': 'Jan Nowak',
            'email': 'example@post.com',
            'phone_number': '123 456 789',
            'message': 'Test contact page message'
        }

        response = self.client.post(
            '/contact',
            data={
                'name': post_data['name'],
                'email': post_data['email'],
                'phone_number': post_data['phone_number'],
                'message': post_data['message']
            }
        )
        self.assertEqual(response.status_code, 302, f'Test failed: status code {response.status_code}')

        user_customer = User.query.filter_by(email=post_data['email'], phone_number=post_data['phone_number']).first()
        email_record = ContactEmail.query.filter_by(email=post_data['email']).first()
        text_message = Message.query.filter_by(text_message=post_data['message']).first()

        self.assertIsNotNone(user_customer, f'Test failed: no user with email {post_data["email"]} in f{User} table')
        self.assertIsNotNone(email_record,
                             f'Test failed: no contact email {post_data["email"]} in f{ContactEmail} table')
        self.assertEqual(user_customer.full_name, post_data['name'])
        self.assertEqual(text_message.user_id, user_customer.id, f"Test failed: Message doesn't exist")

    # Send footer email form
    def test_footer_email_form(self):
        response = self.client.post(
            '/submit_email',
            data={
                'email': 'example@post.com'
            }
        )
        self.assertEqual(response.status_code, 302, f'Test failed: status code {response.status_code}')

        contact_email = ContactEmail.query.filter_by(email='example@post.com').first()

        self.assertIsNotNone(contact_email.email,  f'Test failed: no contact email {contact_email}')
        self.assertEqual(contact_email.email, 'example@post.com', f'Test failed: no contact email {contact_email}')