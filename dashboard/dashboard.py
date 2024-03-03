import streamlit as st
import pandas as pd
import plotly.express as px
from your_module import *

# Membaca data dari file CSV
days_df = pd.read_csv("dashboard/day_clean.csv")
hours_df = pd.read_csv("dashboard/hour_clean.csv")

# Memanggil fungsi visualize_bike_rental
def visualize_bike_rental(day_df):
    # Ekstrak hari dari kolom 'dteday'
    day_df['day_of_week'] = day_df['dteday'].dt.day_name()

    # Mengatur urutan hari dalam seminggu
    day_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # Mengubah kolom 'day_of_week' menjadi tipe kategori dengan urutan yang ditentukan
    day_df['day_of_week'] = pd.Categorical(day_df['day_of_week'], categories=day_order, ordered=True)

    # Ekstrak bulan dari kolom 'dteday'
    day_df['month'] = day_df['dteday'].dt.month

    # Visualisasi rata-rata jumlah peminjaman sepeda berdasarkan hari dalam seminggu
    fig1 = px.line(day_df.groupby('day_of_week')['count_cr'].mean(), markers=True)
    fig1.update_layout(title='Rata-rata Jumlah Peminjaman Sepeda Berdasarkan Hari dalam Seminggu',
                       xaxis_title='Hari dalam Seminggu',
                       yaxis_title='Rata-rata Jumlah Peminjaman Sepeda')
    st.plotly_chart(fig1)

    # Visualisasi rata-rata jumlah peminjaman sepeda berdasarkan bulan dalam setahun
    fig2 = px.line(day_df.groupby('month')['count_cr'].mean(), markers=True)
    fig2.update_layout(title='Rata-rata Jumlah Peminjaman Sepeda Berdasarkan Bulan dalam Setahun',
                       xaxis_title='Bulan dalam Setahun',
                       yaxis_title='Rata-rata Jumlah Peminjaman Sepeda')
    st.plotly_chart(fig2)

# Memanggil fungsi visualize_bike_rental
visualize_bike_rental(days_df)
