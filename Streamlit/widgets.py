import streamlit as st

st.title('StreamLit Text Input')

name = st.text_input("Enter Your Name")
age = st.slider("Select Your Age", 0, 100, 25)
gender = ['Male', 'Female']
choice = st.selectbox("Gender", gender)

if name : 
     st.write(f"Hello, {name}")

if age : 
    st.write(f"Age : {age}")

if choice : 
    st.write(f"Gender : {choice}")