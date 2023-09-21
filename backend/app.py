import sys
sys.path.append('..')
from backend.api import bp_api

from flask import Flask, Blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(bp_api, url_prefix="/api")
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
