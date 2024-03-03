import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from your_module import *

# Membaca data dari file CSV
days_df = pd.read_csv("dashboard/day_clean.csv")
hours_df = pd.read_csv("dashboard/hour_clean.csv")

# Memanggil fungsi find_peak_rental_hour
peak_hour, max_rentals = find_peak_rental_hour(hour_df)
st.write(f"Jam dengan penyewaan sepeda paling banyak: {peak_hour}, Jumlah penyewaan pada jam tersebut: {max_rentals}")

# Memanggil fungsi calculate_peak_hours_usage
peak_hour_usage, non_peak_hour_usage = calculate_peak_hours_usage(hour_df)
st.write(f"Total Penggunaan Sepeda pada Jam Puncak: {peak_hour_usage}, Total Penggunaan Sepeda pada Jam Non-puncak: {non_peak_hour_usage}")

# Memanggil fungsi sum_order
sum_order_items_df = sum_order(hour_df)
st.write(sum_order_items_df)

# Memanggil fungsi macem_season
season_df = macem_season(day_df)
st.write(season_df)

# Memanggil fungsi compare_peak_non_peak
compare_peak_non_peak(peak_hour_usage, non_peak_hour_usage)

# Memanggil fungsi visualize_bike_rental
visualize_bike_rental(day_df)

# Memanggil fungsi visualize_bike_usage_over_time
visualize_bike_usage_over_time(day_df)

# Memanggil fungsi visualize_seasonal_data
visualize_seasonal_data(day_df)
