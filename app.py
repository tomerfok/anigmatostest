import sqlite3
from flask import Flask, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

@app.route('/')
def get():
    return '<h1>Welcome to Flask</h1>'

if __name__ == "__main__":
    app.run(debug=True)
