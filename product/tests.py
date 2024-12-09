from django.test import TestCase
from global_utills.base_test import generate_product
from django.urls import reverse

class TestProductApp (TestCase) :

    def setUp(self):
        self.get_producuts_endpoint = reverse('get_all_products')

    def test_get_empty_product(self) : 
        response = self.client.get(
            self.get_producuts_endpoint
        )
        self.assertEqual(len(response.json()), 0)

    def test_get_nonempty_product(self) : 
        generate_product()
        response = self.client.get(
            self.get_producuts_endpoint
        )
        self.assertNotEqual(len(response.json()), 0)

    def test_retrive_product_notfound(self) : 
        response = self.client.get(
            reverse('get_product_by_id', args=[2])
        )
        self.assertEqual(response.status_code, 404)

    def test_retrive_product_found(self) :
        product = generate_product() 
        response = self.client.get(
            reverse('get_product_by_id', args=[product.id])
        )
        self.assertEqual(response.status_code, 200)
