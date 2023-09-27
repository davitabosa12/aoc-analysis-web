import sys
sys.path.append('..')
from backend.api import bp_api

from flask import Flask, Blueprint, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder="build/static", template_folder="build")
CORS(app)
app.register_blueprint(bp_api, url_prefix="/api")
@app.route("/")
def render_react():
    return render_template("index.html")
