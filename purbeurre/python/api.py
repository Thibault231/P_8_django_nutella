# coding: utf-8
""" Rules the connection with the OpenfoodFact's API.
"""
import requests
from python.food_item import FoodItem
from config import CATEGORIES_LIST
import pprint


def api_extraction_by_category(category):
    """
    Return a list of class food.Food objects implemented with cat_id and
    an API from OpenfoodFacts. Datas are taken from the page "categorie".
    Args:
    category: list (list of food categories)
    Return:
    food_list: list (list of "food.Food")
    Example:
        self._api_extraction(categorie, cat_id)
    """
    response = requests.get(
        ('https://fr.openfoodfacts.org/categorie/{}.json').
        format(category))
    file = response.json()
    food_list = []
    food_items_list = []
    for element in file['products']:
        if ('ingredients_text_fr' in element)\
                and len(element['ingredients_text_fr']) > 5:
            if element['product_name'] not in food_items_list:
                if 'nutriscore_grade' in element:
                    if 'stores' in element:
                        food_item = FoodItem()
                        food_items_list.append(element['product_name'])
                        
                        food_item.url_id = (element['_id'])
                        food_item.brand = (element['brands'])
                        food_item.name = (element['product_name'])
                        food_item.nutriscore = (
                            element['nutriscore_grade'].upper())
                        food_item.description = (
                            element['ingredients_text_fr'])
                        food_item.allergens = (element['allergens_from_ingredients'])
                        food_item.store = (element['stores'])
                        food_item.picture = (element['image_front_url'])

                        food_list.append(food_item)
    return food_list

def food_item_creation(food_item):
    new_food_item = FoodItem.objects.create(
        name = food_item.name,
        brand = food_item.brand,
        description = food_item.description,
        allergens = food_item.allergens,
        nutriscore = food_item.nutriscore,
        store = food_item.store,
        picture = food_item.picture,
        url_OpenFF = food_item.url,
        )
    return new_food_item

def link_cat_food(new_food_item, new_category):
    new_food = Category_Food.objects.create(
        fk_category_id = new_category.id,
        fk_food_id = new_food_item.id
        )

def Db_implementation():
    for category in CATEGORIES_LIST:
        new_category = Category.objects.create(
            name = category
        )
        food_items_list = api_extraction_by_category(category)
        
        for food_item in food_items_list:
            new_food_item = food_item_creation(food_item)
            link_cat_food(new_food_item, new_category)
            print('   Implement FI:',new_food_item.name, ' ,ok')
    print('Implement Cat:',new_category.name, ' ,ok')
