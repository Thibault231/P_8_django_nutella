from django.test import RequestFactory, TestCase
from ..config import TESTS, CATEGORIES_LIST


class DataBaseTestCase(TestCase):
    def setUp(self):
        self.test_const = TESTS
        self.cat_list_const = CATEGORIES_LIST
    
    def tests_TESTS_constant(self):
        test_const = self.test_const
        self.assertIsInstance(test_const, dict)
        self.assertIsNotNone(test_const['name1'])
        self.assertIsNotNone(test_const['name2'])
        self.assertIsNotNone(test_const['RightStatus'])
        self.assertIsNotNone(test_const['UnfoundStatus'])
        self.assertIsNotNone(test_const['WrongStatus'])
    
    def tests_CATEGORIES_LIST_constant(self):
        cat_list_const = self.cat_list_const
        self.assertIsInstance(cat_list_const, list)
        self.assertEqual(len(cat_list_const), 2)