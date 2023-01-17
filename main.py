# import sqlite3
from flask import Flask, request, url_for, flash, redirect
import firebase_admin
from firebase_admin import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\tomer\\AppData\\Roaming\\gcloud\\application_default_credentials.json"
#os.environ["PORT"]="8080"
cred = firebase_admin.credentials.ApplicationDefault()
app = Flask(__name__)
firebase_admin.initialize_app(cred, {
    'projectId': 'anigmatostest',
})

def getProduct(id):

    db = firestore.client()
    products_ref = db.collection(u'products')

    data = products_ref.where(u'id', u'==', 1).get()
    docs = []
    for doc in data:
        ttt = doc.to_dict()
        docs.append(ttt)
        print(f'doc.to_dict: {ttt}')

    print("0000000000000000000000000000000000000000")

    return docs

@app.route('/')
def get():
    data = getProduct(1)
    # return '<h1>Welcome to my Project,</h1>'
    return data;

@app.route('/search', methods=['GET'])
def search():
    try:
        productId = request.args["id"]
        product = getProduct(productId)
        return product
    except Exception as e:
        return e

if __name__ == "__main__":
    #app.run(debug=True, port = 8080)
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))