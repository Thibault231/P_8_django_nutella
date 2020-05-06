from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    allergens = models.TextField(default=None)
    nutriscore = models.CharField(max_length=1)
    store = models.CharField(max_length=100)
    picture = models.URLField()
    url_OpenFF = models.URLField()
    linked_cat = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    history = models.ManyToManyField(FoodItem)

    def __str__(self):
        return "Account of: {0}".format(self.user.username)
    
class Search(models.Model):
    fk_food_id = models.ForeignKey(FoodItem, related_name='food', on_delete=models.CASCADE)
    fk_substitute_id = models.ForeignKey(FoodItem, related_name='substitute', on_delete=models.CASCADE)
    fk_account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_search = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.date_search

