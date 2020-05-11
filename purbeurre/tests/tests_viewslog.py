from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from ..models import Account, FoodItem, Category
from ..config import TESTS


class ViewsLoginTestCase(TestCase):
    def setUp(self):
        self.food2 = FoodItem.objects.create(name=TESTS['name2'], allergens=TESTS['name1'])
        self.category2 = Category.objects.create(name=TESTS['name1'])
        self.food2.linked_cat.add(self.category2)
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username=TESTS['name1'], email=TESTS['name1']+'@gmail.com', password=TESTS['name1'])
        self.account = Account.objects.create (user=self.user)

    def test_right_save_log_page(self):
        right_id = self.food2.id
        self.client.login(email=TESTS['name1']+'@gmail.com', password=TESTS['name1'])
        response = self.client.get(reverse('purbeurre:save', args=(right_id,)))
        self.assertEqual(response.status_code, 200)

    def test_wrong_save_log_page(self):
        self.client.login(email=TESTS['name1']+'@gmail.com', password=TESTS['name1'])
        response = self.client.get(reverse('purbeurre:save', args=(10000,)))
        self.assertEqual(response.status_code, 404)
    
    def test_right_save_unlog_page(self):
        right_id = self.food2.id
        response = self.client.get(reverse('purbeurre:save', args=(right_id,)))
        self.assertEqual(response.status_code, 302)
    
    def test_wrong_save_unlog_page(self):
        response = self.client.get(reverse('purbeurre:save', args=(10000,)))
        self.assertEqual(response.status_code, 302)

    def test_history_log_page(self):
        self.client.login(email=TESTS['name1']+'@gmail.com', password=TESTS['name1'])
        response = self.client.get(reverse('purbeurre:history'))
        self.assertEqual(response.status_code, 200)
    
    def test_history_unlog_page(self):
        right_id = self.food2.id
        response = self.client.get(reverse('purbeurre:history'))
        self.assertEqual(response.status_code, 302)