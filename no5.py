import streamlit as st
import datetime

# Input Number
st.number_input("Pick a number", min_value=1, max_value=100, value=1)

# Email Address
st.text_input("Email address")

# Date Input for Travelling Date
st.date_input("Travelling date", value=datetime.date(2022, 6, 17))

# Time Input for School Time
st.time_input("School time", value=datetime.time(8, 0))

# Text Area for Description
st.text_area("Description")

# File Upload
st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])

# Color Picker
st.color_picker("Choose your favourite color", value="#800080")
