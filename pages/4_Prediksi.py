import streamlit as st
import joblib
import pandas as pd

st.title("🔮 Prediksi Ketersediaan Pangan")

# Load model
model = joblib.load("model/random_forest.pkl")

st.subheader("Masukkan Data")

produksi = st.number_input(
    "Produksi Padi (Ton)",
    min_value=0.0
)

penduduk = st.number_input(
    "Jumlah Penduduk (ribu jiwa)",
    min_value=0.0
)

curah = st.number_input(
    "Curah Hujan (mm)",
    min_value=0.0
)

panen = st.number_input(
    "Luas Panen (Ha)",
    min_value=0.0
)

if st.button("Prediksi"):

    data = pd.DataFrame({
        "Produksi Padi (Ton)":[produksi],
        "Jumlah Penduduk (ribu jiwa)":[penduduk],
        "Curah Hujan (mm)":[curah],
        "Luas Panen (Ha)":[panen]
    })

    hasil = model.predict(data)[0]
    st.success(f"Hasil Prediksi NCPR : {hasil:.2f}")
    if hasil >= 1:
        st.success("🟢 Status : AMAN")
        st.info("Ketersediaan pangan mencukupi dan relatif stabil.")

    elif hasil >= 0.8:
        st.warning("🟡 Status : WASPADA")
        st.info("Ketersediaan pangan mulai menurun, perlu pemantauan.")

    else:
        st.error("🔴 Status : RAWAN")
        st.error("Ketersediaan pangan rendah, perlu penanganan segera.")