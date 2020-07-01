from flask import Flask
from datetime import datetime
import re

myapp = Flask(__name__)


@myapp.route("/")
def hello():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    name = "Jack"

    content = "Hello " + name + ". It's " + formatted_now + \
        " and we're running Azure App Service for Linux"

    return content
    # return "Hello Flask, on Azure App Service for Linux"
