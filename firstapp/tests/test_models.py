from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from firstapp.models import Category, Painting
from django.core.exceptions import ValidationError

class CategoryModelTest(TestCase):
    def test_category_str_representation(self):
        category = Category(name='testing_mock_category')
        self.assertEqual(str(category), 'testing_mock_category')

class PaintingModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='testing_mock_category')
        self.image = SimpleUploadedFile("image.jpg", b"file_content", content_type="image/jpeg")
        self.painting = Painting.objects.create(
            category=self.category,
            title='Sunset',
            description='A beautiful sunset painting',
            image=self.image
        )

    def test_painting_str_representation(self):
        self.assertEqual(str(self.painting), 'Sunset')

    def test_painting_title_not_blank(self):
        self.painting.title = ''
        with self.assertRaises(ValidationError):
            self.painting.full_clean()
