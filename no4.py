import streamlit as st

# Checkbox
st.checkbox("yes")

# Button
st.button("Click")

# Radio buttons
st.radio("Pick your gender", options=["Male", "Female"])

# Select box
st.selectbox("Pick your gender", options=["Male", "Female"])

# Dropdown
st.selectbox("choose a planet", options=["Choose an option", "Mercury", "Venus", "Earth", "Mars"])

# Slider for "Pick a mark"
st.slider("Pick a mark", min_value=0, max_value=50, value=25)

# Display labels "Bad" and "Excellent" below the slider
col1, col2, col3 = st.columns([1, 6, 1])  # Adjust column ratios as needed
with col1:
    st.text("Bad")
with col3:
    st.text("Excellent")

# Slider for "Pick a number"
st.slider("Pick a number", min_value=0, max_value=50, value=9)
