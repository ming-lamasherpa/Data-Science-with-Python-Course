import joblib
import streamlit as st

st.title("MPG Prediction")
st.write("Enter vehicle features to predict Miles Per Gallon (MPG).")

model = None
try:
    model = joblib.load("Linear_Model.pkl")
except Exception as e:
    st.error(f"Unable to load model: {e}")

cylinders = st.number_input("Cylinders", min_value=1, max_value=16, value=4, step=1)
displacement = st.number_input("Displacement", min_value=0.0, value=150.0, step=0.1)
horsepower = st.number_input("Horsepower", min_value=0.0, value=100.0, step=0.1)
weight = st.number_input("Weight", min_value=0.0, value=3000.0, step=1.0)
acceleration = st.number_input("Acceleration", min_value=0.0, value=12.0, step=0.1)
model_year = st.number_input("Model Year", min_value=70, max_value=100, value=76, step=1)

if st.button("Predict MPG"):
    if model is None:
        st.error("Cannot predict because the model could not be loaded.")
    else:
        features = [[cylinders, displacement, horsepower, weight, acceleration, model_year]]
        try:
            prediction = model.predict(features)
            st.success(f"Predicted Miles Per Gallon: {prediction[0]:.2f}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
