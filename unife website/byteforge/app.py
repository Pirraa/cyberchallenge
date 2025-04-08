import os
import secrets

from flask import Flask, request

FLAG = os.getenv('FLAG')

app = Flask(__name__)

app.secret_key = secrets.token_hex(24)

class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return 'Hi ' + self.name + '!'

@app.get(f"/")
def home():
    return '<form method="POST">Insert your name: <input name="name"></form>'

@app.post(f"/")
def home_hi():
    name = request.form.get('name')
    if not name:
        return 'You need to insert a name'
    person = Person(name)
    return f"{person}".format(person=person)