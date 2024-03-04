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

# Menentukan rentang tanggal yang dapat dipilih
min_date_days = day_df["dteday"].min()
max_date_days = day_df["dteday"].max()

# Filter data berdasarkan rentang tanggal yang dipilih
start_date, end_date = st.date_input(
    label='Rentang Waktu',
    min_value=min_date_days,
    max_value=max_date_days,
    value=[min_date_days, max_date_days])

main_df_days = day_df[(day_df["dteday"] >= str(start_date)) & 
                       (day_df["dteday"] <= str(end_date))]
main_df_hour = hour_df[(hour_df["dteday"] >= str(start_date)) & 
                        (hour_df["dteday"] <= str(end_date))]


st.subheader("Peminjaman Sepeda pada jam tertentu")
# Menyiapkan data
categories = ['Peak Hours', 'Non-Peak Hours']
usage = [peak_hour_usage, non_peak_hour_usage]

# Menampilkan plot menggunakan Streamlit
st.bar_chart(usage, labels=categories, colors=['blue', 'orange'])
st.title('Perbandingan Penggunaan Sepeda antara Jam Puncak dan Jam Non-Puncak')
st.xlabel('Waktu')
st.ylabel('Jumlah Penggunaan Sepeda')

st.subheader("Peminjaman Sepeda pada hari dalam seminggu")
# Fungsi untuk menampilkan rata-rata jumlah peminjaman sepeda berdasarkan hari dalam seminggu
def visualize_bike_rental(day_df):
    day_df['day_of_week'] = pd.to_datetime(day_df['dteday']).dt.day_name()
    plt.figure(figsize=(10,4))
    sns.barplot(x=day_df['day_of_week'], y=day_df['count_cr'], estimator='mean')
    plt.title('Rata-rata Jumlah Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Rata-rata Jumlah Peminjaman Sepeda')

    # Simpan plot ke dalam buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Menampilkan plot menggunakan Streamlit
    st.image(buffer, caption='Rata-rata Jumlah Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')

# Memanggil fungsi untuk menampilkan rata-rata jumlah peminjaman sepeda berdasarkan hari dalam seminggu
visualize_bike_rental(day_df)

st.subheader("Peminjaman Sepeda pada bulan dalam setahun")
# Fungsi untuk menampilkan rata-rata jumlah peminjaman sepeda berdasarkan bulan dalam setahun
def visualize_bike_rental_by_month(day_df):
    day_df['month'] = pd.to_datetime(day_df['dteday']).dt.month_name()
    plt.figure(figsize=(12,4))
    sns.barplot(x=day_df['month'], y=day_df['count_cr'], estimator='mean')
    plt.title('Rata-rata Jumlah Peminjaman Sepeda Berdasarkan Bulan dalam Setahun')
    plt.xlabel('Bulan dalam Setahun')
    plt.ylabel('Rata-rata Jumlah Peminjaman Sepeda')

    # Simpan plot ke dalam buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Menampilkan plot menggunakan Streamlit
    st.image(buffer, caption='Rata-rata Jumlah Peminjaman Sepeda Berdasarkan Bulan dalam Setahun')

# Memanggil fungsi untuk menampilkan rata-rata jumlah peminjaman sepeda berdasarkan bulan dalam setahun
visualize_bike_rental_by_month(day_df)

st.subheader("Tren penggunaan sepeda dari waktu ke waktu")
# Fungsi untuk menampilkan tren penggunaan sepeda dari waktu ke waktu
def visualize_bike_usage_over_time(day_df):
    day_df['year'] = pd.to_datetime(day_df['dteday']).dt.year
    yearly_rentals = day_df.groupby('year')['count_cr'].sum()

    # Plot tren penggunaan sepeda dari waktu ke waktu
    fig, ax = plt.subplots(figsize=(10, 4))
    yearly_rentals.plot(marker='o', color='blue', ax=ax)
    ax.set_title('Tren Penggunaan Sepeda dari Waktu ke Waktu')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Jumlah Peminjaman Sepeda')

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)
# Memanggil fungsi untuk menampilkan tren penggunaan sepeda dari waktu ke waktu
visualize_bike_usage_over_time(day_df)
