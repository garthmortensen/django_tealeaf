from django.test import TestCase, RequestFactory
from django.urls import reverse
from firstapp.models import Category, Painting
from firstapp.views import PaintingListView

class HomeViewTest(TestCase):
    def test_template_used(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'firstapp/home.html')

class StatementViewTest(TestCase):
    def test_template_used(self):
        url = reverse('statement')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'firstapp/statement.html')

class ContactViewTest(TestCase):
    def test_template_used(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'firstapp/contact.html')

class ThankYouViewTest(TestCase):
    def test_template_used(self):
        url = reverse('thank_you')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'firstapp/thank_you.html')

# class CategoryListViewTest(TestCase):
#     def test_template_used(self):
#         url = reverse('category_list')
#         response = self.client.get(url)
#         self.assertTemplateUsed(response, 'firstapp/category_list.html')

# /django_tealeaf/media/image.jpg
class PaintingListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.category = Category.objects.create(name='testing_mock_category')
        self.painting = Painting.objects.create(
            category=self.category,
            title='Sunset',
            description='A beautiful sunset painting',
            image='image.jpg'
        )

    def test_get_queryset(self):
        url = reverse('painting_list', kwargs={'category_name': self.category.name})
        request = self.factory.get(url)
        response = PaintingListView.as_view()(request, category_name=self.category.name)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sunset')

    def test_get_context_data(self):
        url = reverse('painting_list', kwargs={'category_name': self.category.name})
        request = self.factory.get(url)
        response = PaintingListView.as_view()(request, category_name=self.category.name)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['page_name'], self.category.name)
