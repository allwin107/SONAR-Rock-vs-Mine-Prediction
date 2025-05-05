# SONAR Rock vs Mine Prediction

This project is a machine learning application that classifies SONAR signals as either **Rock** or **Mine** based on frequency response data. The dataset contains 60 features corresponding to energy values in various frequency bands and a label indicating the object type.

## 📌 Project Overview

- **Goal:** Predict whether a SONAR return is from a Rock or a Mine using supervised learning techniques.
- **Model Used:** Logistic Regression
- **Data Source:** UCI Machine Learning Repository

## 📊 Dataset Description

- **Name:** SONAR Dataset
- **Samples:** 208
- **Features:** 60 numerical attributes (energy levels)
- **Target:** `R` for Rock, `M` for Mine

Each row in the dataset represents the SONAR signal data collected from a single object.

You can find the dataset here: [UCI SONAR Dataset](https://archive.ics.uci.edu/ml/datasets/connectionist+bench+sonar+mines+vs.+rocks)

## 🧰 Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Jupyter Notebook

## 🚀 How to Run

1. Clone the repository:
   ```
   git clone https://github.com/allwin107/SONAR-Rock-vs-Mine-Prediction.git
   cd SONAR-Rock-vs-Mine-Prediction
   ```
3. Install required packages:

    ```
    pip install -r requirements.txt
    ```
3. Open the notebook:
   
    SONAR_Rock_vs_Mine_Prediction.ipynb
   
5. Run all cells to train and test the model.
