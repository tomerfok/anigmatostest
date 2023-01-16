from pymongo import MongoClient
import json

columnWidth = 15;

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["customers"]
    collection = db["customers"]
    data = [
        {"name": "John Smith", "address": "123 Main St"},
        {"name": "Jane Doe", "address": "456 Park Ave"},
        {"name": "Bob Johnson", "address": "789 Elm St"}
    ]
    print('Customers:')
    for x in collection.find({}, {'_id': 0, 'name': 1, 'address': 1}):
        n = x['name']
        a = x['address']
        print (f'{n: <{columnWidth}} | {a: <{columnWidth}}')
except:
    print("An exception occurred")
