from flask import Blueprint, render_template, request
import requests
from dotenv import load_dotenv
import os #built in module that allows communication between the OS
from pprint import pprint

load_dotenv() #loads the .env file 
API_KEY = os.getenv("API_KEY")

jobListing_bp = Blueprint("joblistings", __name__)

#Provides the results of the homepage search bar 
@jobListing_bp.route("/search")
def search_results():

    #Reads the data from the html form the user sends the backend
    title = request.args.get("job-title", "all")
    location = request.args.get("location", "all")
    site = request.args.get("job-site", "all")

    #Sends request from backend to another server
    query = f"{title} jobs in {location} via {site}"

    url = "https://jsearch.p.rapidapi.com/search"

    params = {"query": query, "page": 5, "num_pages": 1, "country": "us", "date_posted": "all"}

    headers = {"x-rapidapi-key": API_KEY, "x-rapidapi-host": "jsearch.p.rapidapi.com"}

    response = requests.get( url, params=params, headers=headers) #Request the data from the API

    returned_data = response.json() #return the JSON data from the API

    # print(f"Json data: {returned_data}")
    pprint(returned_data["data"])

    return render_template("joblistings.html", jobs = returned_data["data"]) #HTML file where the data is going and variable that obtains values from the "data" list

















