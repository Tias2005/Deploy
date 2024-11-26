import pickle
import streamlit as st
import pandas as pd
import numpy as np
import os

# Path model dan dataset
model_path = r'C:\xampp\htdocs\FOLDER_SISTEM_CERDAS\venv\linear_regression_model.sav'
csv_path = r'C:\xampp\htdocs\FOLDER_SISTEM_CERDAS\venv\praktikum\CarPrice_Assignment.csv'

# Load model
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
        
    # Verifikasi jika model memiliki metode 'predict'
    if not hasattr(model, 'predict'):
        raise ValueError("Model yang dimuat bukan model terlatih yang tepat.")
except FileNotFoundError:
    st.error(f"File model tidak ditemukan di path: {model_path}")
    st.stop()
except ValueError as ve:
    st.error(f"Terjadi kesalahan: {ve}")
    st.stop()
except Exception as e:
    st.error(f"Terjadi kesalahan saat memuat model: {e}")
    st.stop()

# Judul aplikasi
st.title('Prediksi Harga Mobil')

# Bagian Dataset
st.header("Dataset")
# Load file CSV
try:
    df1 = pd.read_csv(csv_path)
    st.dataframe(df1)
except FileNotFoundError:
    st.error(f"File CSV tidak ditemukan di path: {csv_path}")
    st.stop()

# Grafik Highway-mpg
st.write("Grafik Highway-mpg")
chart_highwaympg = pd.DataFrame(df1, columns=["highwaympg"])
st.line_chart(chart_highwaympg)

# Grafik curbweight
st.write("Grafik Curbweight")
chart_curbweight = pd.DataFrame(df1, columns=["curbweight"])
st.line_chart(chart_curbweight)

# Grafik horsepower
st.write("Grafik Horsepower")
chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
st.line_chart(chart_horsepower)

# Input nilai dari variable independent
st.header("Masukkan Data untuk Prediksi")
highwaympg = st.number_input('Highway MPG:', min_value=0, max_value=100, step=1)
curbweight = st.number_input('Curb Weight:', min_value=0, max_value=10000, step=100)
horsepower = st.number_input('Horsepower:', min_value=0, max_value=1000, step=10)

# Tombol Prediksi
if st.button('Prediksi'):
    try:
        # Prediksi menggunakan model
        car_prediction = model.predict(np.array([[highwaympg, curbweight, horsepower]]))
        
        # Konversi hasil prediksi ke format mata uang
        harga_mobil_float = float(car_prediction[0])
        harga_mobil_formatted = f"${harga_mobil_float:,.2f}"
        
        # Tampilkan hasil prediksi
        st.subheader("Hasil Prediksi Harga Mobil")
        st.write(f"Estimasi harga mobil: {harga_mobil_formatted}")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")
