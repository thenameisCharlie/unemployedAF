from flask import Blueprint, render_template
import pandas as pd

job_salaries_bp = Blueprint("jobsalaries", __name__)

@job_salaries_bp.route("/jobsalaries")
def job_salaries():

    df = pd.read_excel("data/wages_data_by_state.xlsx")

    

    return render_template("jobsalaries_page.html")