from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from .models import Account, FoodItem, Category
from .config import TESTS

class ConnectionTestCase(TestCase):
    def setUp(self):
        self.food2 = FoodItem.objects.create(name=TESTS['name2'], allergens=TESTS['name1'])
        self.category2 = Category.objects.create(name=TESTS['name1'])
        self.food2.linked_cat.add(self.category2)
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username=TESTS['name1'], email=TESTS['name1']+'@gmail.com', password=TESTS['name1'],
            first_name=TESTS['name1'], last_name=TESTS['name1'])
        self.account = Account.objects.create (user=self.user)
        self.account.history.add(self.food2)
    
    def test_right_connexion_log_page(self):
        response = self.client.login(email=TESTS['name1']+'@gmail.com', password=TESTS['name1'])
        self.assertIs(response, True)
    
    def test_wrong_connexion_log_page(self):
        response = self.client.login(email=TESTS['name1']+'@gmail.com', password=TESTS['name2'])
        self.assertIsNot(response, True)
    
    def test_connexion_page(self):
        response = self.client.get(reverse('connection:connexion'))
        self.assertEqual(response.status_code, 200)

    def test_deconnexion_log_page(self):
        self.client.login(email=TESTS['name1']+'@gmail.com', password=TESTS['name1'])
        response = self.client.get(reverse('connection:deconnexion'))
        self.assertEqual(response.status_code, 200)
    
    def test_deconnexion_unlog_page(self):
        right_id = self.food2.id
        response = self.client.get(reverse('connection:deconnexion'))
        self.assertEqual(response.status_code, 302)
    
    def test_myaccount_log_page(self):
        self.client.login(email=TESTS['name1']+'@gmail.com', password=TESTS['name1'])
        response = self.client.get(reverse('connection:myaccount'))
        self.assertEqual(response.status_code, 200)
    
    def test_myaccount_unlog_page(self):
        response = self.client.get(reverse('connection:myaccount'))
        self.assertEqual(response.status_code, 302)
    
    def test_count_creation_connection_page(self):
        response = self.client.get(reverse('connection:count_creation'))
        self.assertEqual(response.status_code, 200)
    
    def test_right_count_creation_page(self):
        response = self.client.post(reverse('connection:count_creation'), {
            'username':TESTS['name2'],
            'email': TESTS['name2']+'@gmail.com',
            'password1': TESTS['name2'],
            'password2': TESTS['name2']})
        self.assertEqual(response.status_code, 200)
        