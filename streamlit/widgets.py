import streamlit as st
import pandas as pd

st.title("Sample Widget App")
name = st.text_input("Enter your name:", "e.g: Satyaki")


age = st.slider("Select your age:", 0, 100, 25)
if name and age:
    st.write(f"Hello, {name}! Your age is {age}.")

options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Choose an option:", options)
st.write(f"You selected: {selected_option}")

multiselect_options = st.multiselect("Select multiple options:", options, default=["Option 1"])
st.write(f"You selected: {', '.join(multiselect_options)}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
st.write("Here's a sample DataFrame:")
st.dataframe(df)

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write("Uploaded DataFrame:")
    st.dataframe(uploaded_df)