from flask import Flask, request, jsonify, render_template
import numpy as np
import os

app = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')

# Train model in memory (no file system writes)
model = None

def get_model():
    global model
    if model is None:
        print("Training model in memory...")
        try:
            import pandas as pd
            from sklearn.model_selection import train_test_split
            from sklearn.linear_model import LogisticRegression
            
            data_path = os.path.join(os.path.dirname(__file__), '..', 'sonar data.csv')
            sonar_data = pd.read_csv(data_path, header=None)
            X = sonar_data.drop(columns=60, axis=1)
            Y = sonar_data[60]
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)
            model = LogisticRegression(max_iter=1000)
            model.fit(X_train, Y_train)
            print("Model trained successfully in memory")
        except Exception as e:
            print(f"Error training model: {e}")
            raise e
    return model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        trained_model = get_model()
        
        data = request.json
        input_data = data.get('features')
        
        if not input_data:
             return jsonify({'error': 'No input data provided'}), 400
             
        # Convert string input to list of floats if strictly comma separated string
        if isinstance(input_data, str):
            input_data = [float(x.strip()) for x in input_data.split(',')]
            
        if len(input_data) != 60:
             return jsonify({'error': f'Expected 60 features, got {len(input_data)}'}), 400

        # Reshape for prediction
        features = np.array(input_data).reshape(1, -1)
        
        prediction = trained_model.predict(features)
        probability = trained_model.predict_proba(features)
        
        result = 'Rock' if prediction[0] == 'R' else 'Mine'
        confidence = np.max(probability) * 100
        
        return jsonify({
            'prediction': result,
            'confidence': f"{confidence:.2f}%"
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Vercel serverless handler
app = app
