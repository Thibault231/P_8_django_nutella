import pprint
import requests

response = requests.get(
    ('https://fr.openfoodfacts.org/categorie/{}.json').
    format('cassoulet'))
file = response.json()
a = list(file['products'][0].keys())
print(sorted(a))
i=0
for element in file['products']:
    if element['ingredients_text_debug'] is not None:
        print('hello')

