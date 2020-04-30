# coding: utf-8
""" Rule the class 'food_item.FoodItem' """


class FoodItem():
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

if __name__ == "__main__":
    a = FoodItem()
    print(a)