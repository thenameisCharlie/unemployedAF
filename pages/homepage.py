from flask import Blueprint, render_template


homepage_bp = Blueprint("homepage", __name__) 

#Starting point of the website when it first runs
@homepage_bp.route("/") #function that wraps another function to add extra behavior to it (decorator) without changing the function itself
def homepage():
    return render_template("home.html")







