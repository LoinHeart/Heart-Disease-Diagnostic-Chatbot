# Heart Disease Diagnostic Chatbot

This project implements a heart disease diagnostic chatbot using a deep learning model built with Keras, Flask for the backend API, and Streamlit for the front-end interface. The goal is to predict the likelihood of heart disease based on user-provided input.

## Project Structure

- `Chatbot/`
  - **`HDDC.py`**: Streamlit script providing a user interface for interacting with the heart disease prediction model.

- `AIserver/`
  - **`flask.py`**: Flask API server handling predictions. It processes data received from the Streamlit interface and returns prediction results.
  - **`model.keras`**: Trained Keras model file used for making predictions.
  - **`scaler.pkl`**: Scaler file for standardizing input features before making predictions.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd 'Heart Disease Diagnostic Chatbot'
