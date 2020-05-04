from django.test import TestCase
from django.urls import reverse
from .models import Account, FoodItem, Category, Search

class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class DataBaseTestCase(TestCase):

    def setUp(self):
        self.food = FoodItem.objects.create(name='fromage', allergens='laittt')
        self.category = Category.objects.create(name='laittt')
        self.food.linked_cat.add(self.category)
        self.count = Account.objects.create(first_name='fromage',
        last_name='laittt', email='laittt@gmail.com', password='fromagelaittt')

    def test_fooditem_table_args(self):
        food = self.food
        self.assertEqual(food.name, 'fromage')
        self.assertEqual(food.allergens, 'laittt')
        self.assertIsInstance(food.brand, str)
        self.assertIsInstance(food.description, str)
        self.assertIsInstance(food.nutriscore, str)
        self.assertIsInstance(food.store, str)
        self.assertIsInstance(food.url_OpenFF, str)
    
    def test_category_table_args(self):
        category = self.category
        self.assertEqual(category.name, 'laittt')
    
    def test_account_table_args(self):
        count = self.count
        self.assertEqual(count.first_name, 'fromage')
        self.assertEqual(count.last_name, 'laittt')
        self.assertEqual(count.email, 'laittt@gmail.com')
        self.assertEqual(count.password, 'fromagelaittt')
    
    def test_links_food_category_tables(self):
        food = self.food
        category = self.category
        select = FoodItem.objects.get(linked_cat__name__startswith="laittt")
        self.assertEqual(select, food)