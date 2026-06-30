import streamlit as st
import pandas as pd

st.title("🚚 Distribusi Pangan")

# Membaca dataset
df = pd.read_excel("data/Dataset 2020-2024.xlsx")

# Pilih tahun
tahun = st.selectbox(
    "Pilih Tahun",
    sorted(df["Tahun"].unique())
)

df = df[df["Tahun"] == tahun]

# Menentukan status
def status_pangan(x):
    if x >= 1:
        return "🟢 Aman"
    elif x >= 0.8:
        return "🟡 Waspada"
    else:
        return "🔴 Rawan"

df["Status"] = df["Ketersediaan Pangan (NCPR)"].apply(status_pangan)

st.subheader("Status Ketersediaan Pangan")

st.dataframe(
    df[[
        "Kabupaten/Kota",
        "Ketersediaan Pangan (NCPR)",
        "Status"
    ]],
    use_container_width=True
)

st.divider()

st.subheader("📦 Rekomendasi Distribusi")

aman = df[df["Ketersediaan Pangan (NCPR)"] >= 1]

waspada = df[
    (df["Ketersediaan Pangan (NCPR)"] >= 0.8) &
    (df["Ketersediaan Pangan (NCPR)"] < 1)
]

rawan = df[df["Ketersediaan Pangan (NCPR)"] < 0.8]

if len(aman) == 0:
    st.warning("Tidak ada daerah aman sebagai sumber distribusi.")

elif len(rawan) == 0:
    st.success("Tidak ada daerah rawan.")

else:

    jumlah = min(len(aman), len(rawan))

    for i in range(jumlah):

        asal = aman.iloc[i]["Kabupaten/Kota"]
        tujuan = rawan.iloc[i]["Kabupaten/Kota"]

        st.success(f"🚚 {asal} ➜ {tujuan}")

# ===================================
# PETA
# ===================================

st.divider()

st.subheader("🗺️ Peta Distribusi Pangan")

st.image(
    r"D:\Unila\Satria Data\Olah data\assets\peta_lampung.png",
    use_container_width=True
)

st.info("""
🟢 Hijau = Aman

🟡 Kuning = Waspada

🔴 Merah = Rawan
""")

# ===================================
# RINGKASAN
# ===================================

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric(
    "🟢 Aman",
    len(aman)
)

col2.metric(
    "🟡 Waspada",
    len(waspada)
)

col3.metric(
    "🔴 Rawan",
    len(rawan)
)