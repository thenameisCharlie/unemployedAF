from flask import Blueprint


homepage_bp = Blueprint("homepage", __name__)

@homepage_bp.route("/") #function that wraps another function to add extra behavior to it (decorator) without changing the function itself
def home():
    return "homepage"



