from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from ..models import Account, FoodItem, Category
from ..config import TESTS

class ViewsTestCase(TestCase):

    def setUp(self):
        self.food1 = FoodItem.objects.create(name=TESTS['name2'], allergens=TESTS['name1'])
        self.category1 = Category.objects.create(name=TESTS['name1'])
        self.food1.linked_cat.add(self.category1)

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_legal_page(self):
        response = self.client.get(reverse('purbeurre:legal'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_wrong_result_page(self):
        response = self.client.post(reverse('purbeurre:result'), {'item_name':TESTS['name1']})
        self.assertEqual(response.status_code, 404)

    def test_right_result_page(self):
        right_name = self.food1.name
        response = self.client.post(reverse('purbeurre:result'), {'item_name': right_name})
        self.assertEqual(response.status_code, 200)

    def test_right_item_page(self):
        right_id = self.food1.id
        response = self.client.get(reverse('purbeurre:item', args=(right_id,)))
        self.assertEqual(response.status_code, 200)

    def test_wrong_item_page(self):
        response = self.client.get(reverse('purbeurre:item', args=(10000,)))
        self.assertEqual(response.status_code, 404)
