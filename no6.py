import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

# Streamlit header and write examples
st.header('st.write')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)

# Create a DataFrame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Display the DataFrame
st.write(df)

# Display another message with a DataFrame
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Generate random data and create another DataFrame
df2 = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])

# Create a chart using Altair
c = alt.Chart(df2).mark_circle().encode(
    x='a',
    y='b',
    size='c',
    color='c',
    tooltip=['a', 'b', 'c']
)

# Display the chart
st.write(c)
