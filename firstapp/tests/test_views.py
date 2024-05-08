from django.test import TestCase, Client
from django.urls import reverse
from firstapp.views import home, contact, portfolio, statement

# run tests via:
# python manage.py test firstapp.tests.test_views 

class ViewsTestCase(TestCase):
    """
    Test case for the views in the firstapp application.
    """

    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        """
        Test case for the home view.

        This test checks if the home view returns a 200 status code,
        uses the 'firstapp/home.html' template, and contains the text 'Hello, Mars!'.
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'firstapp/home.html')
        self.assertContains(response, 'Hello, Mars!')

    def test_contact_view(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'firstapp/contact.html')

    def test_portfolio_view(self):
        url = reverse('portfolio')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'firstapp/portfolio.html')

    def test_statement_view(self):
        url = reverse('statement')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'firstapp/statement.html')
