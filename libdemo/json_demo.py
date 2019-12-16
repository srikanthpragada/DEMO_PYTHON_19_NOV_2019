import json
from oop.product import Product

p = Product("Abc", 10000)

print(json.dumps(p.__dict__))
