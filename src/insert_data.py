import json

from mongo import client as mongo

mongo.create_index([("$**", "text")])


with open('forms.json', 'r') as f:
    forms = json.load(f)

for form in forms:
    mongo.insert_one(form)
