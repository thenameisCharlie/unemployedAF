from flask import Flask
from pages.homepage import homepage_bp
from pages.joblistings import jobListing_bp 
from pages.jobsalaryresults import jobsalaryresults_bp
from pages.jobsalaries_page import job_salaries_bp

#Blueprints allow you to split routes into Python files and register the blueprint to the main hub (app.py)
app = Flask(__name__)
app.register_blueprint(homepage_bp)
app.register_blueprint(jobListing_bp)
app.register_blueprint(jobsalaryresults_bp)
app.register_blueprint(job_salaries_bp)


if __name__ == "__main__":
    app.run(debug=True)

