from django.test import TestCase
from django.urls import reverse
from category.models import Category

class TestCategoryEndpoints(TestCase) : 

    def test_get_all_categories(self) : 
        response = self.client.get(
            reverse('get_all_categories')
        )
        self.assertEqual(response.status_code, 200)

    def test_get_undefined_category(self) : 
        response = self.client.get(
            reverse('get_category_by_id', args=[1]),
        )
        self.assertEqual(response.status_code, 404)


    def test_get_defined_category(self) : 
        c = Category.objects.create(name='test')
        response = self.client.get(
            reverse('get_category_by_id', args=[c.id]),
        )
        self.assertEqual(response.status_code, 200)