import joblib
import streamlit as st

model = joblib.load('linear_model.pkl')

st.title("Student Perfromance Prediction")
st.subheader("Multiple Linear Regression")


st.write("Enter the values for the features below:")
Hours_Studied = st.number_input("Hours Studied", value=0)
Previous_Scores = st.number_input("Previous Scores", value=0)
Extracurricular_Activities = st.number_input("Extracurricular Activities (Yes=1, No=0)", value=0)
Sleep_Hours = st.number_input("Sleep Hours", value=0)
Sample_Question_Papers_Practiced = st.number_input("Sample Question Papers Practiced", value=0)


if st.button("Predict"):
  
    if Previous_Scores > 100:
        st.error("Invalid Input: Previous Scores cannot exceed 100.")
    
    elif Hours_Studied + Sleep_Hours > 24:
        st.error("Invalid Input: Values ccannot exceed 24.")
   
    else:
        
        user_input = [[
            Hours_Studied,
            Previous_Scores,
            Extracurricular_Activities,
            Sleep_Hours,
            Sample_Question_Papers_Practiced,
        ]]    

        prediction = model.predict(user_input)
        
        if prediction < 0:
            st.success(f"Predicted Value: 0.0")
        elif prediction > 100:
            st.error("Invalid Prediction cannot be greater than 100.0")
        else:
            st.success(f"Predicted Value: {prediction[0]:.2f}")

