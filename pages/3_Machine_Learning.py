from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import joblib
import os
import streamlit as st
import pandas as pd

st.title("🤖 Machine Learning")

df = pd.read_excel("data/Dataset 2020-2024.xlsx")

st.write("Dataset")

st.dataframe(df.head())

st.success("Dataset berhasil dimuat")
st.divider()

st.header("Training Model Random Forest")

# Feature
X = df[
    [
        "Produksi Padi (Ton)",
        "Jumlah Penduduk (ribu jiwa)",
        "Curah Hujan (mm)",
        "Luas Panen (Ha)"
    ]
]

# Target
y = df["Ketersediaan Pangan (NCPR)"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)
# Membuat folder model jika belum ada
os.makedirs("model", exist_ok=True)

# Simpan model
joblib.dump(model, "model/random_forest.pkl")

# Prediksi
prediksi = model.predict(X_test)

# Evaluasi
mae = mean_absolute_error(y_test, prediksi)
rmse = mean_squared_error(y_test, prediksi) ** 0.5
r2 = r2_score(y_test, prediksi)

st.subheader("Evaluasi Model")

col1, col2, col3 = st.columns(3)

col1.metric(
    "MAE",
    round(mae,3)
)

col2.metric(
    "RMSE",
    round(rmse,3)
)

col3.metric(
    "R² Score",
    round(r2,3)
)

st.divider()

hasil = X_test.copy()

hasil["Aktual"] = y_test.values
hasil["Prediksi"] = prediksi

st.subheader("Hasil Prediksi")

st.dataframe(hasil)



