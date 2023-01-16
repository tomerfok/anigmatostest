from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["customers"]
    collection = db["customers"]
    data = [
        {"name": "John Smith", "address": "123 Main St"},
        {"name": "Jane Doe", "address": "456 Park Ave"},
        {"name": "Bob Johnson", "address": "789 Elm St"}
    ]
    collection.insert_many(data)
    print("Sample data inserted successfully")
except:
    print("An exception occurred")
