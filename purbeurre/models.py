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


class FoodItemOFF():
    """
    Class 'food_item.FoodItem'
    Attributs:
    id (int), name(str), cat(str), cat_id(int), market(str),
    descriptions(str), nutriscore(str), url_id(int)
    All attributs are default str('none')
    Class methods:
    -food_item_request
    Example:
    food_item = Food()
    """
    def __init__(self):
        self.name = str()
        self.brand = str()
        self.category = list()
        self.store = str()
        self.description = str()
        self.allergens = str()
        self.nutriscore = str()
        self.url_id = str()
        self.picture = str()


