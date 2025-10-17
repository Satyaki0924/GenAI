import streamlit as st
import pandas as pd
import numpy as np

## Title
st.title("Hello World!")

## Display simple text
st.write("A Quick Brown Fox Jumped Over The Lazy Dog!!!")

## Create a DataFrame
df = pd.DataFrame({
    'Column A': np.random.randn(10),
    'Column B': np.random.randn(10)
})

st.write("Here's a simple DataFrame:")
st.dataframe(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)