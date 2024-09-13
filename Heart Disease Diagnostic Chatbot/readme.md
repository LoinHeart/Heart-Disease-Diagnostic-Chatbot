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
   cd uci_chatbot



Heart Disease Diagnostic Chatbot/
│
├── AIserver/
│   ├── flask.py
│   ├── model.keras
│   └── scaler.pkl
│
├── Chatbot/
│   └── HDDC.py
│
└── README.md
