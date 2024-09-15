# Heart Disease Diagnostic Chatbot

This project is a heart disease diagnostic chatbot built using a Keras-based deep learning model, Flask for the backend API, and Streamlit for the front-end interface. The goal is to predict the likelihood of heart disease based on user-provided input.

## Project Structure

- `Chatbot/`
  - **`HDDC.py`**: The Streamlit script that provides a user interface to interact with the heart disease prediction model.

- `AIserver/`
  - **`flask.py`**: The Flask API server that handles predictions. It receives data from the Streamlit interface, processes it, and returns predictions.
  - **`model.keras`**: The trained Keras model file used for making predictions.
  - **`scaler.pkl`**: The scaler file used to standardize the input features before prediction.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd  'Heart Disease Diagnostic Chatbot'

Install Dependencies:

It’s recommended to use a virtual environment. You can create one using venv or conda, and then install the required packages.
   ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:


pip install tensorflow scikit-learn flask joblib streamlit
Run the Flask Server:

Navigate to the AIserver directory and start the Flask server.


cd AIserver
python flask.py
The server will start and listen for requests on http://127.0.0.1:5000.

Run the Streamlit Interface:

In a separate terminal, navigate to the uci_chatbot directory and start the Streamlit application.


cd Chatbot
streamlit run HDDC.py
The Streamlit interface will be available at http://localhost:8501.

Usage
Interact with the Streamlit Interface:

Open the Streamlit app in your web browser.
Enter the required data (age, sex, chest pain type, etc.) into the provided fields.
Click the "Predict" button to get the heart disease prediction.
Flask API Endpoint:

Endpoint: /predict
Method: POST
Data: JSON object with the required features.
Response: JSON object with the predicted class and a message indicating the likelihood of heart disease.
Example request:


{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
Example response:


{
  "predicted_class": 1,
  "message": "You are likely to have heart disease."
}
Notes
Ensure that Test_Accuracy_84.52%.keras and scaler.pkl are located in the AI_server directory before starting the Flask server.
Adjust paths and configurations according to your environment if necessary.




Feel free to modify the `README.md` to fit your specific needs or project details!






Here is a requirements.txt file for Heart Disease Diagnostic Chatbot, which includes all the necessary packages:

tensorflow==2.13.0
scikit-learn==1.3.0
flask==2.3.3
joblib==1.3.2
streamlit==1.22.0
Instructions for Using requirements.txt
Create a Virtual Environment (if not already created):


python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the Required Packages:


pip install -r requirements.txt
This file will ensure that all the necessary dependencies for running Heart Disease Diagnostic Chatbot are installed in your environment. Adjust package versions if needed based on your specific setup or compatibility requirements.

