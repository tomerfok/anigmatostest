# import sqlite3
from flask import Flask, request, url_for, flash, redirect
import firebase_admin
from firebase_admin import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\tomer\\AppData\\Roaming\\gcloud\\application_default_credentials.json"
cred = firebase_admin.credentials.ApplicationDefault()
app = Flask(__name__)
firebase_admin.initialize_app(cred, {
    'projectId': 'anigmatostest',
})

def getProduct(id):
    
    db = firestore.client()
    products_ref = db.collection(u'products')

    data = products_ref.where(u'id', u'==', id).get()
    docs = []
    for doc in data:
        productDict = doc.to_dict()
        docs.append(productDict)
        print(f'doc.to_dict: {productDict}')

    return docs

@app.route('/')
def get():
    return '<h1>Welcome to my Project,</h1>'

@app.route('/search', methods=['GET'])
def search():
    try:
        productId = request.args["id"]
        productId = int(productId)
        product = getProduct(productId)
        return product
    except Exception as e:
        return e

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))