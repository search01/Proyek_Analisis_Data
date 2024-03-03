import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Fungsi ini digunakan untuk menemukan jam dengan jumlah penyewaan sepeda paling banyak.
def find_peak_rental_hour(df):
    hourly_rentals = df.groupby('hours')['count_cr'].sum()
    jam_max_penyewaan = hourly_rentals.idxmax()
    jumlah_max_penyewaan = hourly_rentals.max()
    return jam_max_penyewaan, jumlah_max_penyewaan
# Panggil fungsi find_peak_rental_hour dengan dataframe yang sesuai sebagai argumennya
peak_hour, max_rentals = find_peak_rental_hour(hour_df)

# Fungsi untuk menghitung total penggunaan sepeda pada jam puncak dan non-puncak.  Misalnya, jam puncak adalah 6-9 pagi dan 4-7 sore
def calculate_peak_hours_usage(dataframe):
    peak_hours = [6, 7, 8, 9, 16, 17, 18, 19]
    dataframe["peak_hour"] = dataframe["hours"].isin(peak_hours)
    peak_hour_usage = dataframe[dataframe["peak_hour"]]["count_cr"].sum()
    non_peak_hour_usage = dataframe[~dataframe["peak_hour"]]["count_cr"].sum()
    return peak_hour_usage, non_peak_hour_usage
# Memanggil fungsi dan menyimpan hasilnya
peak_hour_usage, non_peak_hour_usage = calculate_peak_hours_usage(hour_df)

# Fungsi untuk menghitung total order per jam
def sum_order(hour_df):
    sum_order_items_df = hour_df.groupby("hours").count_cr.sum().sort_values(ascending=False).reset_index()
    return sum_order_items_df

# Fungsi untuk menghitung total penyewaan berdasarkan musim
def macem_season(day_df): 
    season_df = day_df.groupby(by="season").count_cr.sum().reset_index() 
    return season_df

# Membaca data dari file CSV
days_df = pd.read_csv("dashboard/day_clean.csv")
hours_df = pd.read_csv("dashboard/hour_clean.csv")






