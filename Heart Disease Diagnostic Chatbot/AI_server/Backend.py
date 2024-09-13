import pickle
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
import joblib
app = Flask(__name__)

# Load the saved Keras model and Scaler
model = tf.keras.models.load_model(r'Test_Accuracy_84.52%.keras')

# Load the scaler (ensure it's in the same directory)
with open(r'scaler.pkl', 'rb') as f:
    scaler = joblib.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the POST request
    data = request.json
    features = np.array([[
        data['age'], data['sex'], data['cp'], data['trestbps'], data['chol'], 
        data['fbs'], data['restecg'], data['thalach'], data['exang'], 
        data['oldpeak'], data['slope'], data['ca'], data['thal']
    ]])

    # Scale the input data
    scaled_features = scaler.transform(features)

    # Make a prediction
    prediction = model.predict(scaled_features)
    predicted_class = np.argmax(prediction, axis=1)[0]

    # Return the result as JSON
    return jsonify({
        'predicted_class': int(predicted_class),
        'message': 'You are unlikely to have heart disease.' if predicted_class == 0 else 'You are likely to have heart disease.'
    })

if __name__ == '__main__':
    app.run(debug=True)
