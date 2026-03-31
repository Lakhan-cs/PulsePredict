### import flask
## make a bridge b/w model N frontend
import os
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle, joblib

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = joblib.load(f)


# Open the app link N get interface.html
@app.route('/')
def interface():
    return render_template('lpk_input.html')


# Tap on predict N get the output
@app.route('/predict', methods=['POST'])
def predict():
    Age = int(request.form['Age'])
    Sex = int(request.form['Sex'])
    Chest_Pain_Type = int(request.form['Chest_Pain_Type'])
    Resting_Blood_Pressure = float(request.form['Resting_Blood_Pressure'])
    Cholesterol = float(request.form['Cholesterol'])
    Fasting_Blood_Sugar = float(request.form['Fasting_Blood_Sugar'])
    Max_Heart_Rate = float(request.form['Max_Heart_Rate'])
    Smoking = int(request.form['Smoking'])
    Alcohol_Consumption = int(request.form['Alcohol_Consumption'])
    BMI = float(request.form['BMI'])
    Stress_Level = int(request.form['Stress_Level'])
    Family_History = int(request.form['Family_History'])
    Diabetes = int(request.form['Diabetes'])
    Physical_Activity = int(request.form['Physical_Activity'])


    new_data = {
        'Age': [Age],
        'Sex': [Sex],
        'Chest_Pain_Type': [Chest_Pain_Type],
        'Resting_Blood_Pressure': [Resting_Blood_Pressure],
        'Cholesterol': [Cholesterol],
        'Fasting_Blood_Sugar': [Fasting_Blood_Sugar],
        'Max_Heart_Rate': [Max_Heart_Rate],
        'Smoking': [Smoking],
        'Alcohol_Consumption': [Alcohol_Consumption],
        'BMI': [BMI],
        'Stress_Level': [Stress_Level],
        'Family_History': [Family_History],
        'Diabetes': [Diabetes],
        'Physical_Activity': [Physical_Activity]
    }

    new_data_df = pd.DataFrame(new_data)

    prediction = model.predict(new_data_df)[0]


    #  STRONG RISK FACTORS

    if Age > 60:
        prediction += 4
    elif Age > 45:
        prediction += 2

    if Cholesterol > 310:
        prediction +=15
    elif Cholesterol > 280:
        prediction += 10
    elif Cholesterol > 260:
        prediction += 8
    elif Cholesterol > 235:
        prediction += 6
    elif Cholesterol > 200:
        prediction += 4
    elif Cholesterol < 200:
        prediction -= 8


    if Resting_Blood_Pressure > 160:
        prediction += 4
    elif Resting_Blood_Pressure > 140:
        prediction += 2
    elif Resting_Blood_Pressure > 120:
        prediction += 1


    if BMI > 32:
        prediction += 5
    elif BMI > 28:
        prediction += 3
    elif BMI > 25:
        prediction += 1
    elif BMI < 18:
        prediction += 3

    if Diabetes == 1:
        prediction += 4

    if Family_History == 1:
        prediction += 1


    #  MODERATE FACTORS

    if Smoking == 1:
        prediction += 1

    if Alcohol_Consumption == 1:
        prediction += 1

    if Stress_Level >= 9:
        prediction += 2
    elif Stress_Level >= 7:
        prediction += 1

    if Chest_Pain_Type == 0:
        prediction += 5
    elif Chest_Pain_Type == 1:
        prediction += 3
    elif Chest_Pain_Type == 2:
        prediction += 0


    # PROTECTIVE FACTORS

    if Physical_Activity >= 6:
        prediction -= 8
    elif Physical_Activity >= 4:
        prediction -= 5
    elif Physical_Activity >= 2:
        prediction -= 3

    if Max_Heart_Rate > 170:
        prediction -= 7
    elif Max_Heart_Rate > 150:
        prediction -= 5
    elif Max_Heart_Rate > 130:
        prediction -= 3
    
 
    # COMBINATION RULES

    if  Diabetes == 1 and Cholesterol > 230:
        prediction += 4

    if Smoking == 1 and BMI > 30:
        prediction += 2

    if Age > 55 and Resting_Blood_Pressure > 140:
        prediction += 1

    if Physical_Activity >= 3 and BMI < 26:
        prediction -= 5

    if (Smoking==0 or Alcohol_Consumption==0 or Family_History==0 or Age<40 or Diabetes==0):
        prediction -= 4


    # Based on prediction
    if (prediction > 70 and Cholesterol < 250 and Age<60 and Diabetes==0):
        prediction -= 8
    elif (prediction > 70 and Chest_Pain_Type!=0 and Age<60 and Diabetes==0):
        prediction -= 8
    
    if (prediction > 85 and (Cholesterol < 300 or Age<60 or Diabetes==0)):
        prediction -= 10
    elif (prediction > 85 and (Chest_Pain_Type !=0 or Age<60 or Diabetes==0)):
        prediction -= 10
    #  FINAL RANGE FIX

    prediction = max(35, min(95, prediction))


    # FINAL RESULT

    if prediction < 50:
        result = f"Low Risk ({round(prediction,2)}%)"
    elif prediction < 70:
        result = f"Medium Risk ({round(prediction,2)}%)"
    elif prediction < 85:
        result = f"High Risk ({round(prediction,2)}%)"
    else :
        result = f"Very High Risk ({round(prediction,2)}%)"
    

    return render_template("lpk_output.html", result=result)

### Port the app as public host
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render/hosting will give PORT
    app.run(host='0.0.0.0', port=port, debug=False)