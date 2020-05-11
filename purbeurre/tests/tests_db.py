from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from ..models import Account, FoodItem, Category
from ..config import TESTS


class DataBaseTestCase(TestCase):

    def setUp(self):
        self.food = FoodItem.objects.create(name=TESTS['name1'], allergens=TESTS['name2'])
        self.category = Category.objects.create(name=TESTS['name2'])
        self.food.linked_cat.add(self.category)
        self.user = User.objects.create_user(
            username=TESTS['name2'], email=TESTS['name2']+'@gmail.com', password=TESTS['name2'])
        self.account = Account.objects.create (user=self.user)


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
    
   
    def test_links_food_category_tables(self):
        food = self.food
        category = self.category
        select = FoodItem.objects.get(linked_cat__name__startswith=TESTS['name2'])
        self.assertEqual(select, food)
    
    def test_account_table_args(self):
        user = self.user
        account = self.account
        food = self.food
        account.history.add(food)
        history_list = list(account.history.all())
        self.assertEqual(account.user, user)
        self.assertEqual(history_list[0], food)