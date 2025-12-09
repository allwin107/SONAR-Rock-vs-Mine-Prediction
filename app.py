from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
try:
    model = joblib.load('sonar_model.pkl')
except:
    model = None
    print("Model not found. Please run train_model.py first.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model not trained'}), 500

    try:
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
        
        prediction = model.predict(features)
        probability = model.predict_proba(features)
        
        result = 'Rock' if prediction[0] == 'R' else 'Mine'
        confidence = np.max(probability) * 100
        
        return jsonify({
            'prediction': result,
            'confidence': f"{confidence:.2f}%"
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
