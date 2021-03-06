from flask import Flask
from datetime import datetime
import re
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/hello/<name>")
def hello_there(name: str):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d, %B, %Y at %X")
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there," + clean_name + "! It's " + formatted_now
    return content


@app.route("/user/<username>")
def show_user_profile(username: str):
    return "User %s" % escape(username)
