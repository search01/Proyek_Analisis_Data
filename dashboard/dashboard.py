import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from io import BytesIO

st.title('Data Bike Sharing')

# Membaca data dari file CSV
day_df = pd.read_csv("dashboard/day_clean.csv")
hour_df = pd.read_csv("dashboard/hour_clean.csv")

# Melakukan penyesuaian pada kolom datetime
datetime_columns = ["dteday"]
for column in datetime_columns:
    day_df[column] = pd.to_datetime(day_df[column])
    hour_df[column] = pd.to_datetime(hour_df[column])
min_date_days = day_df["dteday"].min()
max_date_days = day_df["dteday"].max()
start_date, end_date = st.date_input(
    label='Rentang Waktu',
    min_value=min_date_days,
    max_value=max_date_days,
    value=[min_date_days, max_date_days])

main_df_days = day_df[(day_df["dteday"] >= str(start_date)) & 
                       (day_df["dteday"] <= str(end_date))]
main_df_hour = hour_df[(hour_df["dteday"] >= str(start_date)) & 
                        (hour_df["dteday"] <= str(end_date))]

# Fungsi untuk menghitung total penggunaan sepeda pada jam puncak dan non-puncak
def calculate_peak_hour_usage(hour_df):
    peak_hours = [6, 7, 8, 9, 16, 17, 18, 19]
    hour_df["peak_hour"] = hour_df["hours"].isin(peak_hours)
    peak_hour_usage = hour_df[hour_df["peak_hour"]]["count_cr"].sum()
    non_peak_hour_usage = hour_df[~hour_df["peak_hour"]]["count_cr"].sum()
    return peak_hour_usage, non_peak_hour_usage
peak_hour_usage, non_peak_hour_usage = calculate_peak_hour_usage(hour_df)

# Menampilkan plot menggunakan Streamlit
st.subheader("Peminjaman Sepeda pada waktu tertentu")
categories = ['Jam Puncak', 'Jam Non - Puncak']
usage = [peak_hour_usage, non_peak_hour_usage]
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(categories, usage, color=['blue', 'orange'])
ax.set_title('Perbandingan Penggunaan Sepeda antara Jam Puncak dan Jam Non-Puncak')
ax.set_xlabel('Waktu')
ax.set_ylabel('Jumlah Penggunaan Sepeda')
st.pyplot(fig)

# Mengkonversi kolom tanggal menjadi tipe data datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df['day_of_week'] = day_df['dteday'].dt.day_name()
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Fungsi untuk menghitung rata-rata penggunaan sepeda berdasarkan hari dalam seminggu
def calculate_daily_average_by_day(day_df):
    daily_average_by_day = day_df.groupby('day_of_week')['count_cr'].mean()
    daily_average_by_day = daily_average_by_day.reindex(days_order)
    return daily_average_by_day
# Menghitung rata-rata penggunaan sepeda berdasarkan hari dalam seminggu
daily_average_by_day = calculate_daily_average_by_day(day_df)

# Menampilkan plot menggunakan Streamlit
st.subheader("Penggunaan Sepeda untuk Setiap Hari dalam Seminggu")
st.bar_chart(daily_average_by_day)


# Menghitung total penyewaan popularitas
total = day_df.groupby(day_df['dteday'].dt.year)[['registered', 'casual']].sum()
total['Total Penyewaan'] = total.sum(axis=1)

# Menampilkan plot menggunakan Streamlit
st.subheader("Popularitas Penyewaan Sepeda pada tahun")
st.bar_chart(total['Total Penyewaan'])

