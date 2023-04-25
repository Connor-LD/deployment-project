### Import Packages
import requests
import pandas as pd
import traceback
# from my_transformers import DenseTransformer


if __name__ == '__main__':
    json_data = {"LoanAmount": 200, 
                 "ApplicantIncome": 7000,
                 "CoapplicantIncome": 0,
                 "Loan_Amount_Term": 360, 
                 "Credit_History": 1, 
                 "Gender": "Female", 
                 "Married": "Yes", 
                 "Dependents": "0", 
                 "Education": "Not Graduate", 
                 "Self_Employed": "No", 
                 "Property_Area": "Urban"}

    URL = "http://127.0.0.1:5000/predict"
    r = requests.post(url = URL, json = json_data) 
    print(r.json())