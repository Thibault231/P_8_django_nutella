from python.api import *

a = api_extraction_by_category('pain')
pprint.pprint(a[0].__dict__)