from flask import Blueprint, render_template

job_salaries_bp = Blueprint("jobsalaries", __name__)

@job_salaries_bp.route("/jobsalaries")
def job_salaries():
    return render_template("jobsalaries_page.html")