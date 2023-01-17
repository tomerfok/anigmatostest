import firebase_admin
from firebase_admin import firestore
# Use the application default credentials
cred = firebase_admin.credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': 'YOUR_PROJECT_ID',
})
db = firestore.client()
products_ref = db.collection(u'products')
data = [
    {"name": "Product 1", "price": 10.99, "description": "Product 1 Description"},
    {"name": "Product 2", "price": 20.99, "description": "Product 2 Description"},
    {"name": "Product 3", "price": 30.99, "description": "Product 3 Description"}
]
for product in data:
    products_ref.add(product)
print("Sample data inserted successfully")
