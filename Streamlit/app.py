import streamlit as st
import pandas as pd
import numpy as np

st.title("hello world")
st.write("this is a simple text")

df = pd.DataFrame(
    {
        'first': [1, 2, 3, 4, 5],
        'second' : [1, 2, 3, 4, 5]
    }
)

st.write("here is your data frame")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns = ['a', 'b', 'c']
)
st.line_chart(chart_data)