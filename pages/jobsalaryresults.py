from flask import Blueprint, request, render_template
import requests
from dotenv import load_dotenv
import os #built in module that allows communication between the OS
from pprint import pprint

load_dotenv() #loads the .env file 
API_KEY = os.getenv("API_KEY")

jobsalaryresults_bp = Blueprint("jobsalaryresults", __name__)

@jobsalaryresults_bp.route("/jobsalaryresults")
def job_salary_results():

    #Reads the data from the html form that the user sends the backend
    salary_job_title = request.args.get("salary-job-title")
    salary_location = request.args.get("salary-location")

    #Sends request from backend to another server
    url = "https://jsearch.p.rapidapi.com/estimated-salary"

    params = {"job_title": salary_job_title, "location": salary_location} 

    headers = {"x-rapidapi-key": API_KEY, "x-rapidapi-host": "jsearch.p.rapidapi.com"} #Data required for the server to recognize the user

    response = requests.get(url, params=params, headers=headers) #response from the server with data

    data = response.json() #converts data to json

    pprint(data)

    return render_template("jobsalaryresults.html", salaries = data["data"]) #renders the html file and returns the value of the "data" key

    

    


    
