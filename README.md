# Heart-Disease-Prediction-Machine-learning
A Heart Disease Prediction model using Machine learning 

## Screenshots![Screenshot 2023-01-12 at 17-12-33 app · Streamlit](https://user-images.githubusercontent.com/120994590/212121812-51903759-d083-4340-ac48-bcbece031749.png)


## Data set
- Description : 
    - The dataset used provides informations ( 13 medical parameters ) on the risk factors for heart disease
- Attributes : 
    - Age : Patients Age  ( Numeric )
    - Sex : Gender of patient  (Male , Female )
    - CP :  Type of chest pain experienced by patient (1 : typical, 2 : typical angina, 3 : non-anginal pain, 4 : asymptomatic)
    - Trestbps :Level of blood pressure at resting mode in mm/HG  ( Numeric )
    - Chol : Serum cholestrol in mg/dl (Numeric)
    - Fbs : Blood sugar levels on fasting > 120 mg/dl  ( Numeric )
    - Restecg : Result of electrocardiogram (O : Normal , 1 : Abnormality in ST-T wave ,2 : Left ventricular hypertrophy)
    - Thalach : Maximum Heart Rate achieved ( Numeric )
    - Exang : Exercise Induced Angina ( Numeric )
    - Oldpeak : Exercise induced ST-depression ( Numeric )
    - Slope : ST segment measured in terms of slope during peak ( Numeric )
    - Ca : Major vessels colored by flourosopy
    -Thal : Thalassemia ( normal , fixed , defect )
    
 - Target variable :
    - 1 : means patient is suffering from heart risk 
    - 0 : means patient is normal.
    
## Project Overview : 
This project is devided into two parts  : 
- Creation and Training model : 
    - /data/heart_disease_data.csv : Dataset CSV File
    - /code/ModelTraining.ipynb : Model source code file 
    -  /code/model.sav : Model saved 
- Ui : using Streamlit tool
    - /app.py : Main file of the ui 
 
## Getting started

1. Clone the repository
2. install required python packages if previously not installed
3. Switch to the project directory
4. Run the ModelTraining.ipynb step by step (This will retrain the model)
5. Run `streamlit run app.py` to run the web UI

        
