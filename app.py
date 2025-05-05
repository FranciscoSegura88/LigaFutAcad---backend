from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
