# Importing essential libraries
from flask import Flask, render_template, request
import joblib,pickle
import numpy as np

app = Flask(__name__)
# Load the regression model
classifier = joblib.load('hr_ana.pkl')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    Age = (request.form['Age']) 
    BusinessTravel = (request.form['BusinessTravel'])
    Department = (request.form['Department'])
    DistanceFromHome = float(request.form['DistanceFromHome'])
    Education = (request.form['Education'])
    EducationField = (request.form['EducationField'])
    Gender = (request.form['Gender'])
    JobLevel = (request.form['JobLevel'])
    JobRole = (request.form['JobRole'])
    MaritalStatus = (request.form['MaritalStatus'])
    MonthlyIncome = float(request.form['MonthlyIncome'])
    NumCompaniesWorked = (request.form['NumCompaniesWorked'])
    PercentSalaryHike = float(request.form['PercentSalaryHike'])
    StockOptionLevel = (request.form['StockOptionLevel'])
    TotalWorkingYears = float(request.form['TotalWorkingYears'])
    TrainingTimesLastYear = float(request.form['TrainingTimesLastYear'])
    YearsAtCompany = float(request.form['YearsAtCompany'])
    YearsSinceLastPromotion = float(request.form['YearsSinceLastPromotion'])
    YearsWithCurrManager = float(request.form['YearsWithCurrManager'])


    data = [[ Age, BusinessTravel, Department, DistanceFromHome,Education, EducationField, Gender, JobLevel, JobRole,MaritalStatus, MonthlyIncome, NumCompaniesWorked, PercentSalaryHike, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, YearsAtCompany, YearsSinceLastPromotion, YearsWithCurrManager]]

    if (Age == 0 and BusinessTravel == 0 and Department == 0):
        my_prediction = [0]
    else:
        my_prediction = classifier.predict(data)
        if my_prediction == 0:
            return render_template('index.html', prediction_text='The Employee will leave the organisation')
        else:
            return render_template('index.html', prediction_text='The Employee will stay in  the organisation')

    



if __name__ == "__main__":
    app.run(debug=True)