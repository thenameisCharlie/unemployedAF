from flask import Blueprint, request, render_template
import pandas as pd

jobsalaryresults_bp = Blueprint("jobsalaryresults", __name__)

@jobsalaryresults_bp.route("/jobsalaryresults")
def job_salary_results():

    #Reads the data from the html form that the user sends the backend
    job_title = request.args.get("job-salary-title", "").strip()
    job_location = request.args.get("job-salary-location", "").strip()
    
    df = pd.read_excel("data/wages_data_by_state.xlsx") #read the excel file 

    #created a list of all the columns with string values that should be numeric
    wage_cols = ["A_MEAN","A_PCT10","A_PCT90","H_MEAN","H_PCT10","H_PCT90"]

    #loop 
    for c in wage_cols:
        df[c] = (
            df[c]
            .astype(str)                                  # force everything to string
            .str.replace(r"[^\d.]", "", regex=True)       # keep only digits and decimal
            .pipe(pd.to_numeric, errors="coerce")         # convert to float, bad ones → NaN
        )

    #Filter DataFrame to rows that match the OCC_TITLE column by the job title that the user sends in the HTML form (case insensitve)
    #This line of code is saying "Give me the rows where the OCC_TITLE column matches what I’m looking for."(data in job_title/job_location)
    filtered_data = df[df["OCC_TITLE"].str.contains(job_title, case=False, na=False) &
                        df["AREA_TITLE"].str.contains(job_location, case=False, na=False)]
    
    

    
    #turns the table into a list of dicts and making it one dict per row (orient="records")
    #Note [[]] is for the DataFrame and [] is for a Series which doesn't work with .to_dict()
    job_wages = filtered_data[["OCC_TITLE", "AREA_TITLE", "H_MEAN", "A_MEAN", "H_PCT10", "H_PCT90", "A_PCT10", "A_PCT90"]].to_dict(orient="records") 

    #render the html file, left variable: name the html template will use, right variable: python variable
    return render_template("jobsalaryresults.html", job_wages=job_wages)

#Note add Exception handling 
