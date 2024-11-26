import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pickle
import os

# Judul Aplikasi
st.title('Aplikasi Prediksi Harga Mobil')
st.sidebar.header("Navigasi")
menu = st.sidebar.selectbox("Pilih Halaman", ["Dataset", "Visualisasi", "Prediksi Harga"])

# Load dataset
df = pd.read_csv(r'C:\xampp\htdocs\Deploy\CarPrice_Assignment.csv')
st.sidebar.write(f"Total data: {len(df)}")

# Fungsi untuk menyimpan model
def save_model(model, filename=r'C:\xampp\htdocs\Deploy\linear_regression_model.sav'):
    pickle.dump(model, open(filename, 'wb'))

# Fungsi untuk memuat model
def load_model(filename=r'C:\xampp\htdocs\Deploy\linear_regression_model.sav'):
    if os.path.exists(filename):
        return pickle.load(open(filename, 'rb'))
    else:
        return None

# Jika menu adalah Dataset
if menu == "Dataset":
    st.subheader("Dataset Mobil")
    st.dataframe(df)

    # Statistik deskriptif
    st.subheader("Statistik Deskriptif")
    st.write(df.describe())

    # Data kosong
    st.subheader("Data Kosong")
    missing_data = df.isnull().sum()
    st.write(missing_data)

# Jika menu adalah Visualisasi
elif menu == "Visualisasi":
    st.subheader("Visualisasi Data Mobil")

    # Distribusi harga mobil
    st.subheader("Distribusi Harga Mobil")
    fig, ax = plt.subplots()
    sns.histplot(df["price"], kde=True, color="blue", ax=ax)
    st.pyplot(fig)

    # Distribusi jumlah mobil berdasarkan nama
    st.subheader("Distribusi Jumlah Mobil Berdasarkan Nama")
    car_counts = df['CarName'].value_counts().head(10)
    fig, ax = plt.subplots()
    car_counts.plot(kind="bar", color="skyblue", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Scatter plot antara highway-mpg dan price
    st.subheader("Hubungan antara Highway MPG dan Harga")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df['highwaympg'], y=df['price'], color="purple", ax=ax)
    plt.xlabel("Highway MPG")
    plt.ylabel("Price")
    st.pyplot(fig)

    # Visualisasi distribusi unik nama mobil
    st.subheader("Distribusi Unik Nama Mobil")
    unique_car_counts = df['CarName'].value_counts().sort_values(ascending=False)
    fig, ax = plt.subplots()
    unique_car_counts.head(10).plot(kind="bar", ax=ax, color="green")
    plt.title("Top 10 Mobil Berdasarkan Jumlah")
    plt.xlabel("Nama Mobil")
    plt.ylabel("Frekuensi")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Jika menu adalah Prediksi Harga
elif menu == "Prediksi Harga":
    st.subheader("Prediksi Harga Mobil")

    # Pemisahan fitur dan target
    X = df[['highwaympg', 'curbweight', 'horsepower']]
    y = df['price']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Latih model
    model = LinearRegression()
    model.fit(X_train, y_train)
    save_model(model)

    # Input pengguna
    st.write("Masukkan Spesifikasi Mobil:")
    highway_mpg = st.number_input('Highway MPG', min_value=0.0, max_value=100.0, value=25.0)
    curbweight = st.number_input('Curb Weight', min_value=0, max_value=5000, value=2500)
    horsepower = st.number_input('Horsepower', min_value=0, max_value=500, value=150)

    # Prediksi berdasarkan input
    if st.button("Prediksi"):
        loaded_model = load_model()
        if loaded_model:
            input_data = pd.DataFrame({'highwaympg': [highway_mpg], 'curbweight': [curbweight], 'horsepower': [horsepower]})
            predicted_price = loaded_model.predict(input_data)[0]
            st.write(f"Harga mobil yang diprediksi: ${predicted_price:,.2f}")
        else:
            st.write("Model tidak ditemukan, harap latih model terlebih dahulu.")

    # Evaluasi model
    model_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, model_pred)
    mse = mean_squared_error(y_test, model_pred)
    rmse = np.sqrt(mse)

    st.write("\n### Evaluasi Model:")
    st.write(f"Mean Absolute Error (MAE): {mae:.2f}")
    st.write(f"Mean Squared Error (MSE): {mse:.2f}")
    st.write(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
