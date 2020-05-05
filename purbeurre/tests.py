from django.test import TestCase
from django.urls import reverse
from .models import Account, FoodItem, Category, Search
from .config import TESTS

class DataBaseTestCase(TestCase):

    def setUp(self):
        self.food = FoodItem.objects.create(name=TESTS['name1'], allergens=TESTS['name2'])
        self.category = Category.objects.create(name=TESTS['name2'])
        self.food.linked_cat.add(self.category)
        self.count = Account.objects.create(first_name=TESTS['name1'],
        last_name=TESTS['name2'], email=TESTS['name2']+'@gmail.com', password=TESTS['name2']+TESTS['name1'])

    def test_fooditem_table_args(self):
        food = self.food
        self.assertEqual(food.name, TESTS['name1'])
        self.assertEqual(food.allergens, TESTS['name2'])
        self.assertIsInstance(food.brand, str)
        self.assertIsInstance(food.description, str)
        self.assertIsInstance(food.nutriscore, str)
        self.assertIsInstance(food.store, str)
        self.assertIsInstance(food.url_OpenFF, str)
    
    def test_category_table_args(self):
        category = self.category
        self.assertEqual(category.name, TESTS['name2'])
    
    def test_account_table_args(self):
        count = self.count
        self.assertEqual(count.first_name, TESTS['name1'])
        self.assertEqual(count.last_name, TESTS['name2'])
        self.assertEqual(count.email, TESTS['name2']+'@gmail.com')
        self.assertEqual(count.password, TESTS['name2']+TESTS['name1'])
    
    def test_links_food_category_tables(self):
        food = self.food
        category = self.category
        select = FoodItem.objects.get(linked_cat__name__startswith=TESTS['name2'])
        self.assertEqual(select, food)


class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])


class ResultPageTestCase(TestCase):
    def test_result_page(self):
        response = self.client.get(reverse('purbeurre:result'), item_name=TESTS['name1'])
        self.assertEqual(response.status_code, TESTS['RightStatus'])