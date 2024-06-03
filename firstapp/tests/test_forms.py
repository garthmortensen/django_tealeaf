from django.test import TestCase
from django.urls import reverse
from firstapp.forms import ContactForm
from unittest.mock import patch
from django.core import mail


class ContactFormTestCase(TestCase):
    """
    Test cases for the ContactForm class and contact form in the firstapp application.
    """

    def setUp(self):
        self.url = reverse('contact')
        self.response = self.client.get(self.url, follow=True)  # Follow any initial redirects

    def test_contact_form_status_code(self):
        """
        Test that the contact page responds with a 200 status code.
        """
        self.assertEqual(self.response.status_code, 200)

    def test_contact_form_template_used(self):
        """
        Test that the correct template is used for the contact form.
        """
        self.assertTemplateUsed(self.response, 'firstapp/contact.html')

    def test_contact_form_contains_form(self):
        """
        Test that the form is present in the response context.
        """
        form = self.response.context['form']
        self.assertIsInstance(form, ContactForm)

    def test_contact_form_csrf(self):
        """
        Test that the rendered form contains a CSRF token.
        """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_valid_contact_form(self):
        """
        Test that the contact form is valid with valid data.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test message',
            'captcha': '5'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_contact_form(self):
        """
        Test that the contact form is invalid with invalid data.
        """
        form_data = {
            'name': '',
            'email': 'john@example',
            'subject': '',
            'message': 'Test',
            'captcha': 'wrong'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_clean_email(self):
        """
        Test the clean_email method of the contact form.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test message',
            'captcha': '5'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['email'], 'john@example.com')

    def test_clean_captcha(self):
        """
        Test the clean_captcha method of the contact form.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test message',
            'captcha': 'wrong'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('captcha', form.errors)
        self.assertEqual(form.errors['captcha'][0], 'Incorrect answer for CAPTCHA.')

    def test_contact_form_valid_data(self):
        """
        Test form submission with valid data.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test message',
            'captcha': '5'  # Assuming the answer to your CAPTCHA is always '5' for test simplicity
        }
        with patch('django.core.mail.send_mail') as mock_send:
            response = self.client.post(self.url, form_data, follow=True)
            self.assertTrue(mock_send.called)
            self.assertEqual(response.status_status_code, 302)  # Check if there is a redirect after a successful post

    def test_contact_form_invalid_data(self):
        """
        Test form submission with invalid data.
        """
        form_data = {
            'name': '',
            'email': 'john@example',  # Incorrect email format
            'subject': '',
            'message': 'Test',  # This might be valid depending on min_length settings
            'captcha': 'wrong'  # Incorrect CAPTCHA
        }
        response = self.client.post(self.url, form_data, follow=True)
        self.assertEqual(response.status_code, 200)  # Ensure the page reloads with errors
        self.assertTrue(response.context['form'].errors)  # Ensure form errors are present


    # Additional tests
    def test_contact_form_name_required(self):
        """
        Test that the name field is required.
        """
        form_data = {
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test message',
            'captcha': '5'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_contact_form_email_required(self):
        """
        Test that the email field is required.
        """
        form_data = {
            'name': 'John Doe',
            'subject': 'Test Subject',
            'message': 'Test message',
            'captcha': '5'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_contact_form_subject_required(self):
        """
        Test that the subject field is required.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Test message',
            'captcha': '5'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors)
        self.assertEqual(form.errors['subject'][0], 'This field is required.')

    def test_contact_form_message_required(self):
        """
        Test that the message field is required.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'captcha': '5'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    def test_contact_form_captcha_required(self):
        """
        Test that the captcha field is required.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test message',
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('captcha', form.errors)
        self.assertEqual(form.errors['captcha'][0], 'This field is required.')
