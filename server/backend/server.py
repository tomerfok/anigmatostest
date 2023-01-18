from flask import Flask, request
import firebase_admin
from firebase_admin import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\tomer\\AppData\\Roaming\\gcloud\\application_default_credentials.json"

cred = firebase_admin.credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': 'anigmatostest',
})

app = Flask(__name__)

def insertCustomer(customer):
    db = firestore.client()
    customers_ref = db.collection(u'customers')
    customers_ref.add(customer)    

@app.route('/', methods=['GET'])
def get():
    return '<h1>Welcome to my Project,</h1>'

@app.route('/create', methods=['GET', 'POST'])
def search():
    try:
        customer = request.get_json()
        insertCustomer(customer)
        return "Succefully created customer record"
    except Exception as e:
        return e

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))