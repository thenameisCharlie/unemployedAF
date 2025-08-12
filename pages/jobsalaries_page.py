from flask import Blueprint, render_template
import pandas as pd

job_salaries_bp = Blueprint("jobsalaries", __name__)

@job_salaries_bp.route("/jobsalaries")
def job_salaries():

    #Read the excel sheet
    df = pd.read_excel("data/wages_data_by_state.xlsx")
    
    #Used a mask to turn the list/Series of True/False. Keep the rows that meet the condition (True)
    #This still returns all the filtered columns where the rows meet the condition
    top_wages_data = df[df["A_MEAN"] > 100000]

    #Narrows the DataFrame to just the columns that are needed
    top_wages = top_wages_data[["OCC_TITLE", "AREA_TITLE","A_MEAN"]].to_dict(orient="records")

    return render_template("jobsalaries_page.html", top_wages=top_wages)