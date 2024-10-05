import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Muat data
data = pd.read_csv('dashboard/cleaned_data.csv') 

# Title Dashboard
st.title('Dashboard Analisis E-Commerce')
st.write('Analisis data e-commerce untuk mendapatkan wawasan dari penjualan dan pelanggan.')

# Pertanyaan 1: Kategori produk terlaris
st.subheader('10 Kategori Produk Terlaris')
produk_terlaris = data['product_category_name_english'].value_counts().head(10)

# kategori produk terlaris
fig1, ax1 = plt.subplots()
sns.barplot(x=produk_terlaris.index, y=produk_terlaris.values, ax=ax1, palette='viridis')
ax1.set_title('10 Kategori Produk Terlaris')
ax1.set_xlabel('Kategori Produk')
ax1.set_ylabel('Jumlah Pembelian')
plt.xticks(rotation=45)
st.pyplot(fig1)

# Pertanyaan 2: Kota dengan jumlah pelanggan terbanyak
st.subheader('Metode Pembayaran Terpopuler')
metode_pembayaran = data['payment_type'].value_counts()

# Visualisasi metode pembayaran
fig3, ax3 = plt.subplots()
sns.barplot(x=metode_pembayaran.index, y=metode_pembayaran.values, ax=ax3, palette='viridis')
ax3.set_title('Metode Pembayaran Terpopuler')
ax3.set_xlabel('Metode Pembayaran')
ax3.set_ylabel('Jumlah Transaksi')
plt.xticks(rotation=45)
st.pyplot(fig3)

# Pertanyaan 3: Metode pembayaran terpopuler
st.subheader('10 Kota dengan Jumlah Pelanggan Terbanyak')
city_customers = data['customer_city'].value_counts().head(10)

# kota dengan jumlah pelanggan terbanyak
fig2, ax2 = plt.subplots()
sns.barplot(x=city_customers.values, y=city_customers.index, ax=ax2, palette='viridis')
ax2.set_title('10 Kota dengan Pelanggan Terbanyak')
ax2.set_xlabel('Jumlah Pelanggan')
ax2.set_ylabel('Kota')
st.pyplot(fig2)

# Interaksi: Filter berdasarkan kota
city_filter = st.selectbox('Pilih Kota untuk Analisis Lebih Lanjut:', data['customer_city'].unique())
filtered_data = data[data['customer_city'] == city_filter]

st.subheader(f'Data Pelanggan di {city_filter}')
st.dataframe(filtered_data)

# Informasi tambahan tentang kategori produk terlaris di kota yang dipilih
st.subheader(f'Kategori Produk Terlaris di {city_filter}')
produk_terlaris_kota = filtered_data['product_category_name'].value_counts().head(10)

fig4, ax4 = plt.subplots()
sns.barplot(x=produk_terlaris_kota.index, y=produk_terlaris_kota.values, ax=ax4, palette='viridis')
ax4.set_title(f'10 Kategori Produk Terlaris di {city_filter}')
ax4.set_xlabel('Kategori Produk')
ax4.set_ylabel('Jumlah Pembelian')
plt.xticks(rotation=45)
st.pyplot(fig4)
