import pickle
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, redirect
import joblib
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load the saved Keras model and Scaler
model = tf.keras.models.load_model('Test_Accuracy_84.52%.keras')

# Load the scaler (ensure it's in the same directory)
with open('scaler.pkl', 'rb') as f:
    scaler = joblib.load(f)

@app.route('/')
def home():
    return redirect("http://localhost:8501")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the POST request
        data = request.json
        features = np.array([[data.get('age'), data.get('sex'), data.get('cp'), data.get('trestbps'), data.get('chol'),
                              data.get('fbs'), data.get('restecg'), data.get('thalach'), data.get('exang'),
                              data.get('oldpeak'), data.get('slope'), data.get('ca'), data.get('thal')]])

        # Ensure all fields are provided
        if None in features[0]:
            return jsonify({'error': 'Missing data for prediction'}), 400

        # Scale the input data
        scaled_features = scaler.transform(features)

        # Make a prediction (adjustable threshold)
        prediction_probs = model.predict(scaled_features)[0][0]  # Get the probability for class 1

        # Set a custom threshold, e.g., 0.45
        threshold = 0.45
        predicted_class = 1 if prediction_probs >= threshold else 0

        # Log the incoming request and prediction
        logging.info(f"Features: {features}, Prediction: {predicted_class}, Probability: {prediction_probs:.2f}")

        # Return the result as JSON with confidence
        return jsonify({
            'predicted_class': int(predicted_class),
            'confidence': float(prediction_probs),
            'message': 'You are unlikely to have heart disease.' if predicted_class == 0 else 'You are likely to have heart disease.'
        })

    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        return jsonify({'error': 'Prediction failed', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
