from flask import Blueprint, render_template, request


jobListing_bp = Blueprint("joblistings", __name__)

#Provides the results of the homepage search bar 
@jobListing_bp.route("/search")
def search_results():

    #Reads the data from the html form the user sends the backend
    title = request.args.get("title", "all")
    location = request.args.get("location", "all")
    site = request.args.get("site", "all")

    #Sends request from backend to another server
    query = f"{title} jobs in {location} via {site}"

    url = "https://jsearch.p.rapidapi.com/search"

    params = {"query": query}

    headers = {"x-rapidapi-key": API_KEY, "x-rapidapi-host": "jsearch.p.rapidapi.com"}







