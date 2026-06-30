import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="SPADDY",
    page_icon="🌾",
    layout="wide"
)

# Judul
st.title("🌾 SPADDY")
st.subheader("Sistem Prediksi Distribusi Pangan Berbasis Data")
st.write("Provinsi Lampung")

st.markdown("---")

# Membaca dataset
df = pd.read_excel("data/Dataset 2020-2024.xlsx")

# Menampilkan dataset
st.header("Dataset")
st.dataframe(df)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Kabupaten",
    df["Kabupaten/Kota"].nunique()
)

col2.metric(
    "Jumlah Data",
    len(df)
)

col3.metric(
    "Rata Produksi",
    f"{df['Produksi Padi (Ton)'].mean():,.0f}"
)

col4.metric(
    "Rata NCPR",
    round(df["Ketersediaan Pangan (NCPR)"].mean(),2)
)

st.sidebar.title("🌾 SPADDY")

menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "Dashboard",
        "Visualisasi",
        "Machine Learning",
        "Prediksi",
        "Distribusi"
    ]
)

tahun = st.sidebar.selectbox(
    "Pilih Tahun",
    sorted(df["Tahun"].unique())
)

df_filter = df[df["Tahun"] == tahun]

import plotly.express as px

st.subheader("Produksi Padi per Kabupaten")

fig = px.bar(
    df_filter,
    x="Kabupaten/Kota",
    y="Produksi Padi (Ton)",
    color="Produksi Padi (Ton)",
    text_auto=".2s"
)

fig.update_layout(
    xaxis_title="Kabupaten/Kota",
    yaxis_title="Produksi (Ton)"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Ketersediaan Pangan (NCPR)")

fig2 = px.line(
    df,
    x="Tahun",
    y="Ketersediaan Pangan (NCPR)",
    color="Kabupaten/Kota",
    markers=True
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("📊 Produksi Padi")

...

st.divider()

st.subheader("📈 NCPR")

...

st.divider()

st.subheader("🌧 Curah Hujan")