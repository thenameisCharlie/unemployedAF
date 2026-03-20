from flask import Blueprint, render_template
import pandas as pd

job_salaries_bp = Blueprint("jobsalaries", __name__)

@job_salaries_bp.route("/jobsalaries")
def job_salaries():

    #Read the excel sheet
    df = pd.read_excel("data/wages_data_by_state.xlsx")

    job_salary = df["A_MEAN"]
    
    #converts the column to numeric values and coerce is to ensure no NaN results crashes the code.
    #A_MEAN column is the salary of positions
    job_salary = pd.to_numeric(job_salary, errors="coerce")

    #Used a mask to turn the list/Series of True/False. Keep the rows that meet the condition (True)
    #This still returns all the filtered columns where the rows meet the condition
    top_wages_data = df[job_salary > 150000]

    #Retruns 6 rows of the DataFrame and randomizes them 
    randomized_top_wages = top_wages_data.sample(n=6, random_state=None)

    #Narrows the DataFrame to just the columns that are needed for display
    top_wages = randomized_top_wages[["OCC_TITLE","A_MEAN"]].to_dict(orient="records")

    return render_template("jobsalaries_page.html", top_wages=top_wages)