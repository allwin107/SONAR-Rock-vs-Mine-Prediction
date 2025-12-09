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

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/allwin107/SONAR-Rock-vs-Mine-Prediction.git
   cd SONAR-Rock-vs-Mine-Prediction
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model:
   ```bash
   python train_model.py
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

### Web Interface

The application features a modern, glassmorphic web interface called **EchoDetect** that allows you to:
- Input 60 comma-separated sonar frequency values
- Load sample data for Rock or Mine predictions
- Get real-time predictions with confidence scores
- View results with visual indicators

## 🌐 Deployment

This application is configured for deployment on Vercel. The `vercel.json` file contains the necessary configuration for serverless deployment.
