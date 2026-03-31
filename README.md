# 🫀 Pulse Predict

* **VAC Digital Empowerment | Topic: Healthcare & Nutrition ( Term End Project )**

Pulse Predict is a machine learning-based web application designed to predict an individual's risk of experiencing a heart attack. By analyzing key medical vitals and lifestyle habits, this tool provides a quick and accessible cardiovascular health assessment.

## Software,Tools  & Requirements

1. [GithubAccount](https://github.com/Lakhan-cs)
2. [HerukuAccount](https://dashboard.heroku.com/apps#)
3. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Commond-Line)

* Clone the repo - /folder

```git clone <https://github.com/Lakhan-cs/PulsePredict.git>
```

* Create new enviroments - cmd (predictenv)

```conda create -p predictenv python==3.12.7 -y
conda activate predictenv
```

* Install the library from requirements.txt

```pip install -r requirements.txt
```

## Features

* **Comprehensive Health Form:** Evaluates critical parameters including Age, Blood Pressure, Cholesterol, BMI, and lifestyle habits.
* **Instant Prediction:** Utilizes a trained Scikit-Learn machine learning model (`model.pkl`) to calculate risk probability instantly.
* **Modern UI:** Clean, responsive, and professional medical-themed interface.

## 📁 Project Structure

```text
PulsePredict/
│
├── static/                   # Contains CSS files for styling
│   ├── lpk_input.css
│   └── lpk_output.css
│
├── templates/                # Contains HTML frontend files
│   ├── lpk_input.html        # The main data entry form
│   └── lpk_output.html       # The prediction result page
│
├── lpk_heartdataset.csv      # The dataset used for training the model
├── lpk.py                    # The main Flask application backend
├── model.pkl                 # The pre-trained machine learning model
├── PulsePredict.ipynb        # Jupyter Notebook with data exploration and model training
├── requirements.txt          # List of Python dependencies
├── .gitignore                # Git ignore rules
└── LICENSE                   # MIT License
```
