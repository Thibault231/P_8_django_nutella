from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.first_name


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

    
class Search(models.Model):
    fk_food_id = models.ForeignKey(FoodItem, related_name='food', on_delete=models.CASCADE)
    fk_substitute_id = models.ForeignKey(FoodItem, related_name='substitute', on_delete=models.CASCADE)
    fk_account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_search = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.date_search

