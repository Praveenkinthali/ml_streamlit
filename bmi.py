import streamlit as st


# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


# Title of the application
st.title("BMI Calculator")

# Input fields
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, step=0.1)
height = st.number_input("Enter your height (in meters):", min_value=0.0, step=0.01)

# Calculate BMI when the user clicks the button
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        st.success(f"Your BMI is {bmi:.2f}")

        # Interpret BMI result
        if bmi < 18.5:
            st.info("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.info("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Please enter valid weight and height.")

# Footer
st.write("Powered by Streamlit")
