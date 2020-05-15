# coding: utf-8
"""Define global variables
for PurBeurre APP program.
"""


CATEGORIES_LIST = [
    [
        'acras', 'endives-au-jambon', 'cassoulets',
        'pains-aux-raisins', 'brioches-tranchees',
        'croissants-fourres', 'yaourts-natures',
        'laits-concentres', 'milkfat', 'biscuits',
        'sauces-tomates-au-basilic', 'aiolis', 'guacamoles',
        'pizzas-au-chorizo', 'pizzas-chevre-lardons',
        'chocolats-noirs-sales', 'jus-d-orange'
        ],
    [
        'Plats préparés', 'Viennoiseries', 'Produits laitiers',
        'Sauces', 'Pizzas', 'Snacks sucrés'
        ]
    ]

TESTS = {
    "name1": "impossible",
    "name2": "hellfest",
    "RightStatus": 200,
    "UnfoundStatus": 404,
    "WrongStatus": 302,
    "UrlApp": "https://djangonutella.herokuapp.com/",
    "UrlResult": "https://djangonutella.herokuapp.com/purbeurre/result/",
    "UrlHistory": "https://djangonutella.herokuapp.com/purbeurre/history/",
    "UrlAccount": "https://djangonutella.herokuapp.com/connection/myaccount/",
    "UrlCreation":
    "https://djangonutella.herokuapp.com/connection/count_creation/",
    "UrlConnexion":
    "https://djangonutella.herokuapp.com/connection/connexion/",
    "UrlItem": "https://djangonutella.herokuapp.com/purbeurre/item/21/",
    "UrlSave": "https://djangonutella.herokuapp.com/purbeurre/save/21/",
    "UrlDeconnexion":
    "https://djangonutella.herokuapp.com/connection/deconnexion/"
}
