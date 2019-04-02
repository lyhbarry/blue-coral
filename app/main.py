import os

from flask import Flask
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)
app.config.from_mapping(
    FLASK_ENV=os.environ.get('FLASK_ENV')
)

@app.route("/")
def hello():
    return "Hello, World!"
