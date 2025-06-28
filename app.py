from flask import Flask
from pages.homepage import homepage_bp
from pages.joblistings import jobListing_bp 
from pages.jobsalaries import jobsalaries_bp


app = Flask(__name__)
app.register_blueprint(homepage_bp)
app.register_blueprint(jobListing_bp)
app.register_blueprint(jobsalaries_bp)


if __name__ == "__main__":
    app.run(debug=True)

