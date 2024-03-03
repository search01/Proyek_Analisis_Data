import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fungsi ini digunakan untuk menemukan jam dengan jumlah penyewaan sepeda paling banyak.
def find_peak_rental_hour(df):
    hourly_rentals = df.groupby('hours')['count_cr'].sum()
    jam_max_penyewaan = hourly_rentals.idxmax()
    jumlah_max_penyewaan = hourly_rentals.max()
    return jam_max_penyewaan, jumlah_max_penyewaan

# Fungsi untuk menghitung total penggunaan sepeda pada jam puncak dan non-puncak.  Misalnya, jam puncak adalah 6-9 pagi dan 4-7 sore
def calculate_peak_hours_usage(dataframe):
    peak_hours = [6, 7, 8, 9, 16, 17, 18, 19]
    dataframe["peak_hour"] = dataframe["hours"].isin(peak_hours)
    peak_hour_usage = dataframe[dataframe["peak_hour"]]["count_cr"].sum()
    non_peak_hour_usage = dataframe[~dataframe["peak_hour"]]["count_cr"].sum()
    return peak_hour_usage, non_peak_hour_usage

# Fungsi untuk menghitung total order per jam
def sum_order(hour_df):
    sum_order_items_df = hour_df.groupby("hours").count_cr.sum().sort_values(ascending=False).reset_index()
    return sum_order_items_df

# Fungsi untuk menghitung total penyewaan berdasarkan musim
def macem_season(day_df): 
    season_df = day_df.groupby(by="season").count_cr.sum().reset_index() 
    return season_df

# Membaca data dari file CSV
day_df = pd.read_csv("dashboard/day_clean.csv")
hour_df = pd.read_csv("dashboard/hour_clean.csv")

# Fungsi bike sharing di jam puncak dan non - puncak
def compare_peak_non_peak(peak_hour_usage, non_peak_hour_usage):
    # Menyiapkan data
    categories = ['Peak Hours', 'Non-Peak Hours']
    usage = [peak_hour_usage, non_peak_hour_usage]

    # Membuat plot
    plt.figure(figsize=(6, 4))
    plt.bar(categories, usage, color=['blue', 'orange'])
    plt.title('Perbandingan Penggunaan Sepeda antara Jam Puncak dan Jam Non-Puncak')
    plt.xlabel('Waktu')
    plt.ylabel('Jumlah Penggunaan Sepeda')
    plt.show()

# Fungsi untuk memvisualisasikan rata-rata jumlah peminjaman sepeda berdasarkan hari dalam seminggu dan bulan dalam setahun
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
    plt.figure(figsize=(6,4))
    day_df.groupby('day_of_week')['count_cr'].mean().plot(marker='o')
    plt.title('Rata-rata Jumlah Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Rata-rata Jumlah Peminjaman Sepeda')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    # Visualisasi rata-rata jumlah peminjaman sepeda berdasarkan bulan dalam setahun
    plt.figure(figsize=(6,4))
    day_df.groupby('month')['count_cr'].mean().plot(marker='o')
    plt.title('Rata-rata Jumlah Peminjaman Sepeda Berdasarkan Bulan dalam Setahun')
    plt.xlabel('Bulan dalam Setahun')
    plt.ylabel('Rata-rata Jumlah Peminjaman Sepeda')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.grid(True)
    plt.show()

# Fungsi tren dalam jangka panjang
def visualize_bike_usage_over_time(day_df):
    # Konversi kolom 'dteday' ke tipe data datetime
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])

    # Ekstrak tahun dari kolom 'dteday'
    day_df['year'] = day_df['dteday'].dt.year

    # Hitung jumlah total peminjaman sepeda per tahun
    yearly_rentals = day_df.groupby('year')['count_cr'].sum()

    # Visualisasi tren penggunaan sepeda dari waktu ke waktu
    plt.figure(figsize=(6, 4))
    yearly_rentals.plot(marker='o', color='blue')
    plt.title('Tren Penggunaan Sepeda dari Waktu ke Waktu')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    plt.grid(True)
    plt.xticks(yearly_rentals.index)
    plt.show()
