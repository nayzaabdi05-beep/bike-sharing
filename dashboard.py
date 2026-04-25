import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# --- CONFIG DASHBOARD ---
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Custom CSS untuk mempercantik UI
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD DATA ---
@st.cache_data
def load_data():
    day_df = pd.read_csv("day.csv")
    hour_df = pd.read_csv("hour.csv")
    day_df["dteday"] = pd.to_datetime(day_df["dteday"])
    hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])
    return day_df, hour_df

day_df, hour_df = load_data()

# --- HEADER ---
st.title("🚲 Bike Sharing Analytics Dashboard")
st.markdown("<p style='text-align: center;'>Visualisasi Data Penyewaan Sepeda Berdasarkan Parameter Cuaca dan Waktu</p>", unsafe_allow_html=True)
st.divider()

# --- METRIC SECTION (Biar lebih bagus tampilannya) ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Penyewaan", f"{day_df.cnt.sum():,}")
with col2:
    st.metric("Rata-rata Harian", f"{int(day_df.cnt.mean()):,}")
with col3:
    st.metric("Kondisi Cuaca Maks", f"{day_df.weathersit.max()}")
with col4:
    st.metric("Total Data", f"{len(day_df)}")

st.divider()

# --- VISUALISASI UTAMA ---
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("📌 Pola Penyewaan: Hari Kerja vs Libur")
    fig1 = plt.figure(figsize=(10, 6))
    sns.lineplot(x="hr", y="cnt", hue="workingday", data=hour_df, ci=None, marker="o")
    plt.title("Perbedaan Pola Penyewaan Sepeda: Hari Kerja vs Hari Libur", fontsize=14)
    plt.xlabel("Jam (00:00 - 23:00)", fontsize=12)
    plt.ylabel("Rata-rata Jumlah Penyewaan", fontsize=12)
    plt.legend(title="Tipe Hari", labels=["Hari Libur", "Hari Kerja"])
    plt.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig1)

with row1_col2:
    st.subheader("📌 Dampak Cuaca Terhadap Penyewaan")
    fig2 = plt.figure(figsize=(10, 6))
    sns.barplot(x="weathersit", y="cnt", data=day_df, palette="coolwarm", estimator=np.mean)
    plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca", fontsize=14)
    plt.xlabel("Kondisi Cuaca (1: Cerah, 2: Mendung, 3: Hujan/Salju)", fontsize=12)
    plt.ylabel("Rata-rata Jumlah Penyewaan", fontsize=12)
    st.pyplot(fig2)

st.divider()

# --- HEATMAP SECTION ---
st.subheader("🌡️ Heatmap Korelasi Variabel Cuaca")
fig3 = plt.figure(figsize=(12, 5))
sns.heatmap(day_df[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr(), annot=True, cmap='coolwarm')
plt.title("Heatmap Korelasi Variabel Cuaca terhadap Jumlah Penyewaan")
st.pyplot(fig3)

# --- DATASET EXPLORER ---
with st.expander("🔍 Lihat Detail Statistik Deskriptif"):
    st.write(day_df.describe())

st.caption("Copyright © 2026 | Analisis Data Proyek")