from django.test import TestCase
# Create your tests here.

from .models import Category, Article

class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test 
        Category.objects.create(category='Innovations', 
                                slug='innovations')

    def test_get_absolute_url(self):
        category=Category.objects.get(id=1)

        self.assertEqual(category.get_absolute_url(),
        '/articles/category/innovations')

class ArticleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Article.objects.create(title ="test",
                               slug = "testS")
