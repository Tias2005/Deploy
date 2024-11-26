import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# Path dataset
file_path = r"C:\xampp\htdocs\FOLDER_SISTEM_CERDAS\venv\praktikum\CarPrice_Assignment.csv"

# Load dataset
df_mobil = pd.read_csv(file_path)

# Menampilkan dataset
print("Dataset:")
print(df_mobil)

# Check for missing data
missing_data = df_mobil.isnull().sum()
print("\nMissing data in each column:")
print(missing_data)

# Tampilkan statistik deskriptif
summary_stats = df_mobil.describe()
print("\nSummary statistics:")
print(summary_stats)

# Tambahkan median secara manual
median_values = df_mobil.median(numeric_only=True)
print("\nMedian values (50%):")
print(median_values)

# Menampilkan tipe data setiap kolom
data_types = df_mobil.dtypes
print("\nTipe data pada setiap kolom:")
print(data_types)

# Plot distribusi harga mobil
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title('Car Price Distribution Plot')
sns.histplot(df_mobil['price'])
plt.show()

# Plot distribusi nama mobil
car_counts = df_mobil['CarName'].value_counts()
plt.figure(figsize=(10, 6))
car_counts.plot(kind="bar")
plt.title("CarName Distribution")
plt.xlabel("CarName")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Top 10 nama mobil
top_10_cars = df_mobil['CarName'].value_counts().head(10)
print("\n10 Nama Mobil Terbanyak:")
print(top_10_cars)

# Membuat WordCloud
car_names = " ".join(df_mobil['CarName'])
wordcloud = WordCloud(
    width=800, height=400,
    background_color='white',
    colormap='viridis',
    random_state=42
).generate(car_names)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Car Names", fontsize=16)
plt.show()

# Plot scatter antara highwaympg dan price
plt.scatter(df_mobil['highwaympg'], df_mobil['price'])
plt.xlabel('highwaympg')
plt.ylabel('price')
plt.title('Scatter Plot of highwaympg vs price')
plt.show()

# Linear Regression Model
X = df_mobil[['highwaympg', 'curbweight', 'horsepower']]
y = df_mobil['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training model
model_regresi = LinearRegression()
model_regresi.fit(X_train, y_train)

# Predicting
model_regresi_pred = model_regresi.predict(X_test)

# Visualisasi prediksi vs actual
plt.scatter(X_test.iloc[:, 0], y_test, label='Actual Prices', color='blue')
plt.scatter(X_test.iloc[:, 0], model_regresi_pred, label='Predicted Prices', color='red')
plt.xlabel('highwaympg')
plt.ylabel('price')
plt.legend()
plt.title("Actual vs Predicted Prices")
plt.show()

# Prediksi harga untuk input tertentu
X_new = np.array([[32, 2338, 75]])
predicted_price = model_regresi.predict(X_new)
print("\nPredicted price for input [32, 2338, 75]:", predicted_price)

# Mengubah nilai input menjadi integer
X_new_int = X_new.astype(int)
print("\nInput as integers:", X_new_int)

# Evaluasi model
mae = mean_absolute_error(y_test, model_regresi_pred)
mse = mean_squared_error(y_test, model_regresi_pred)
rmse = np.sqrt(mse)

print(f'\nMean Absolute Error (MAE): {mae:.2f}')
print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'Root Mean Squared Error (RMSE): {rmse:.2f}')

# Menyimpan model ke file .sav
model_filename = "linear_regression_model.sav"
joblib.dump(model_regresi, model_filename)
print(f"\nModel saved to {model_filename}")
