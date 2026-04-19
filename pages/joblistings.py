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
    title = request.args.get("home-job-title", "all")
    location = request.args.get("location", "all")
    site = request.args.get("job-site", "all")

    #Sends request from backend to another server
    query = f"{title} jobs in {location} via {site}" #query was created as a sentence since that's how you make the request to the server (doesn't have separate params)

    url = "https://jsearch.p.rapidapi.com/search"

    params = {"query": query, "page": 1, "num_pages": 1, "country": "us", "date_posted": "all"}

    headers = {"x-rapidapi-key": API_KEY, "x-rapidapi-host": "jsearch.p.rapidapi.com"}

    try:
        response = requests.get( url, params=params, headers=headers) #Request the data from the API
        returned_data = response.json() #return the JSON data from the API
        print(response.status_code)
        print(returned_data)

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")

    pprint(returned_data["data"])

    return render_template("joblistings.html", jobs = returned_data["data"]) #HTML file where the data is going and returning the value of the "data" key and assigning it to jobs

















