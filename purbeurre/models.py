# coding: utf-8
"""Defines models for PurBeurre APP.

Models:
-Category
-FoodItem
-Account
-FoodItemOFF
"""
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Model Category
    Arguments:
    models {Model}
    Attributs:
    -name
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        """Define verbose_name
        """
        verbose_name = "category"

    def __str__(self):
        """Return name when Category object
        is called
        Returns:
            [str] -- attribute name
        """
        return self.name


class FoodItem(models.Model):
    """Model FoodItem
    Arguments:
    models {Model}
    Attributs:
    -name
    -brand
    -description
    -allergens
    -nutriscore
    -store
    -picture
    -url_OpenFF
    -linked_cat
    """
    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    allergens = models.TextField(default=None)
    nutriscore = models.CharField(max_length=1)
    store = models.CharField(max_length=100)
    picture = models.URLField()
    url_OpenFF = models.URLField()
    linked_cat = models.ManyToManyField(Category)

    class Meta:
        """Define verbose_name
        """
        verbose_name = "fooditem"

    def __str__(self):
        """Return name when FoodItem object
        is called
        Returns:
            [str] -- attribute name
        """
        return self.name


class Account(models.Model):
    """Model Account
    Arguments:
    models {Model}
    Attributs:
    -user (oneToOne link)
    -history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    history = models.ManyToManyField(FoodItem)

    class Meta:
        """Define verbose_name
        """
        verbose_name = "account"

    def __str__(self):
        """Return name when Account object
        is called
        Returns:
            [str] -- attribute name
        """
        return "Account of: {0}".format(self.user.username)


class FoodItemOFF():
    """
    Class 'food_item.FoodItem'
    Attributs:
    id (int), name(str), cat(str), cat_id(int), market(str),
    descriptions(str), nutriscore(str), url_id(int)
    All attributs are default str('none')
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
