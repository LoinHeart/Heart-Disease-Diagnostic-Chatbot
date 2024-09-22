import streamlit as st
import requests
import json

# Function to gather user input
def get_user_input():
    age = st.number_input('Age', min_value=28, max_value=77, value=30)
    sex = st.selectbox('Sex (1 = Male, 0 = Female)', [0, 1])
    cp = st.selectbox('Chest Pain Type (0-3)', [0, 1, 2, 3])
    trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200, value=120)
    chol = st.number_input('Cholesterol Level', min_value=100, max_value=600, value=200)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)', [0, 1])
    restecg = st.selectbox('Resting Electrocardiographic Results (0-2)', [0, 1, 2])
    thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
    exang = st.selectbox('Exercise Induced Angina (1 = Yes, 0 = No)', [0, 1])
    oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=6.0, value=1.0, step=0.1)
    slope = st.selectbox('Slope of Peak Exercise ST Segment (0-2)', [0, 1, 2])
    ca = st.number_input('Number of Major Vessels (0-4)', min_value=0, max_value=4, value=0)
    thal = st.selectbox('Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)', [0, 1, 2])

    # Create a dictionary with the user input
    user_data = {
        'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps, 'chol': chol,
        'fbs': fbs, 'restecg': restecg, 'thalach': thalach, 'exang': exang,
        'oldpeak': oldpeak, 'slope': slope, 'ca': ca, 'thal': thal
    }

    return user_data

# Main function for Streamlit app
def main():
    st.title("Heart Disease Diagnostic Chatbot")

    # Gather input data from user
    user_input = get_user_input()

    # When user clicks 'Predict' button, send data to Flask API
    if st.button("Predict"):
        # Send POST request to AI_server API
        url = 'http://127.0.0.1:5000/predict'  # AI_server API URL
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(user_input), headers=headers)

        if response.status_code == 200:
            prediction = response.json()
            st.write(f"Prediction: {prediction['message']}")
            st.write(f"Probability of Heart Disease: {prediction['confidence']:.2%}")
        else:
            st.write("Error: Could not connect to AI Server.")

if __name__ == "__main__":
    main()
