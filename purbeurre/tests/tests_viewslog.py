# coding: utf-8
"""[summary]Unitary Test views.py functions which use
user's loging.
"""
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from ..models import Account, FoodItem, Category
from ..config import TESTS


class ViewsLoginTestCase(TestCase):
    """Class TestCase for tests functions.

    Functions:
    -setUp(self)
    -test_right_save_log_page(self)
    -test_wrong_save_log_page(self)
    -test_right_save_unlog_page(self)
    -test_wrong_save_unlog_page(self)
    -test_history_log_page(self)
    -test_history_unlog_page(self)
    """
    def setUp(self):
        """Create self objects for running tests
        """
        self.food2 = FoodItem.objects.create(
            name=TESTS['name2'], allergens=TESTS['name1'])
        self.category2 = Category.objects.create(name=TESTS['name1'])
        self.food2.linked_cat.add(self.category2)
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username=TESTS['name1'],
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        self.account = Account.objects.create(user=self.user)

    def test_right_save_log_page(self):
        """Test the loging connection to page Save
        """
        right_id = self.food2.id
        self.client.login(
            email=TESTS['name1']+'@gmail.com', password=TESTS['name1'])
        response = self.client.get(reverse('purbeurre:save', args=(right_id,)))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_wrong_save_log_page(self):
        """Test the loging connection to page Save
        with wrong email.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('purbeurre:save', args=(10000,)))
        self.assertEqual(response.status_code, TESTS['UnfoundStatus'])

    def test_right_save_unlog_page(self):
        """Test the unloging connection to page Save
        """
        right_id = self.food2.id
        response = self.client.get(reverse('purbeurre:save', args=(right_id,)))
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_wrong_save_unlog_page(self):
        """Test the unloging connection to page Save
        with wrong email.
        """
        response = self.client.get(reverse('purbeurre:save', args=(10000,)))
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_history_log_page(self):
        """Test the loging connection to page History
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('purbeurre:history'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_history_unlog_page(self):
        """Test the unloging connection to page Save
        """
        response = self.client.get(reverse('purbeurre:history'))
        self.assertEqual(response.status_code, TESTS['WrongStatus'])
