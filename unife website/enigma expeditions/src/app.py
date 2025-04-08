import os
import secrets

from flask import Flask, request

FLAG = os.getenv('FLAG')

app = Flask(__name__)

app.secret_key = secrets.token_hex(24)

@app.get(f"/")
def home():
    file = request.args.get('file')
    if not file:
        return '<ul><li><a href="/?file=lorem">Lorem ipsum</a></li><li><a href="/?file=space">Space ipsum</a></li></ul>'
    while '../' in file:
        file = file.replace('../', '')
    try:
        with open(os.path.join(os.getcwd(), file)) as f:
            data = f.read()
        return data
    except:
        return 'Not found', 404
