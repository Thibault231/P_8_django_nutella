from django.test import RequestFactory, TestCase
from ..config import TESTS


class DataBaseTestCase(TestCase):
    def setUp(self):
        self.test_const = TESTS
        
    def tests_TESTS_constant(self):
        test_const = self.test_const
        self.assertIsInstance(test_const, dict)
        self.assertIsNotNone(test_const['name1'])
        self.assertIsNotNone(test_const['name2'])
        self.assertIsNotNone(test_const['RightStatus'])
        self.assertIsNotNone(test_const['UnfoundStatus'])
        self.assertIsNotNone(test_const['WrongStatus'])
