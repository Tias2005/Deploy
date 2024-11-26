import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sidebar for navigation with only Home
page = st.sidebar.selectbox("Select Page", ["Home"])

# Home Page with an Image, Dataset, and Charts
if page == "Home":
    st.title("Welcome to the Streamlit Web")
    st.image(r"C:\xampp\htdocs\FOLDER_SISTEM_CERDAS\venv\image.png", caption="Image Example", use_container_width=True)

    # Display dataset below the image
    st.subheader("Dataset Preview")

    # Load the dataset
    df = pd.read_csv(r"C:\xampp\htdocs\FOLDER_SISTEM_CERDAS\venv\praktikum\DataScience_salaries_2024.csv")
    st.write(df.head())  # Show a preview of the dataset

    # Check if 'Job Title' and 'Salary' columns are available for plotting the bar chart
    if 'Job Title' in df.columns and 'Salary' in df.columns:
        st.subheader("Bar Chart of Average Salary by Job Title")
        
        # Calculate average salary by job title
        salary_by_job_title = df.groupby('Job Title')['Salary'].mean().sort_values(ascending=False)
        
        # Create a bar chart
        fig, ax = plt.subplots()
        salary_by_job_title.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_title('Average Salary by Job Title')
        ax.set_xlabel('Job Title')
        ax.set_ylabel('Average Salary')
        ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better visibility
        st.pyplot(fig)

    # Displaying a chart below the dataset
    st.subheader("Random Data Chart")

    # Example DataFrame for Chart
    df_chart = pd.DataFrame(np.random.randn(100, 2), columns=["x", "y"])

    # Chart options
    chart_option = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])

    if chart_option == "Line Chart":
        st.line_chart(df_chart)

    elif chart_option == "Bar Chart":
        st.bar_chart(df_chart)

    elif chart_option == "Area Chart":
        st.area_chart(df_chart)
