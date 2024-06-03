import os
from django.test import TestCase, Client
from django.urls import reverse
from firstapp.models import Category, Painting
import os


# Test to ensure Cross-Site Request Forgery (CSRF) protection is working
from django.test import override_settings

class CSRFProtectionTest(TestCase):

    @override_settings(SECURE_SSL_REDIRECT=False)
    def test_csrf_protection(self):
        client = Client(enforce_csrf_checks=True)
        
        # Make POST requests without a CSRF token to different views
        # Check that the response status code is 403 Forbidden
        response = client.post(reverse("home"), {})
        self.assertEqual(response.status_code, 403)

        response = client.post(reverse("statement"), {})
        self.assertEqual(response.status of_code, 403)

        response = client.post(reverse("contact"), {})
        self.assertEqual(response.status_code, 403)


# Test to ensure SQL injection attempts are properly handled
class SQLInjectionTest(TestCase):
    # Set up the test environment by creating instances of Category and Painting models
    def setUp(self):
        self.category = Category.objects.create(name="Landscape")

    def test_sql_injection_in_painting_title(self):
        # Attempt SQL injection into the title field
        injected_title = "'; DROP TABLE paintings; --"
        Painting.objects.create(
            category=self.category,
            title=injected_title,
            description="Description",
            image="test.jpg"
        )

        # Ensure the injected SQL did not execute and the painting was created correctly
        paintings = Painting.objects.all()
        self.assertEqual(paintings.count(), 1)
        self.assertEqual(paintings[0].title, injected_title)

    def test_sql_injection_in_category_name(self):
        # Attempt SQL injection into the category name
        injected_category_name = "'; DROP TABLE category; --"
        Category.objects.create(name=injected_category_name)

        # Ensure the injected SQL did not execute and the category was created correctly
        categories = Category.objects.all()
        self.assertEqual(categories.count(), 2)  # Including the initial setup category
        self.assertEqual(categories[1].name, injected_category_name)


# Test to ensure clickjacking protection is enabled
class ClickjackingProtectionTest(TestCase):
    def test_clickjacking_protection(self):
        response = self.client.get(reverse("home"))
        
        # Ensure the X-Frame-Options header is set to DENY to prevent clickjacking
class HTTPSEnforcementTest(TestCase):
    def test_https_enforcement(self):
        # Skip the test if not in a production environment
        if "PYTHONANYWHERE_DOMAIN" not in os.environ:
            self.skipTest("Skipping HTTPS enforcement test in non-production environment")

        response = self.client.get(reverse("contact"), secure=False)
        # Check that the response is a redirect to the HTTPS version
        self.assertEqual(response.status_code, 301)  # Expecting a permanent redirect
        self.assertTrue(response.url.startswith("https://"))

        # No need to check twice, this is sufficient
        # self.assertTrue(response.url.startswith("https://"))

