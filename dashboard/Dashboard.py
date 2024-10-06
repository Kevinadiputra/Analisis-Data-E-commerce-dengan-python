import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set theme and style for visualizations
sns.set(style="whitegrid")

# Muat data
data = pd.read_csv('dashboard/cleaned_data.csv') 

# Set page layout
st.set_page_config(page_title='Dashboard Analisis E-Commerce', layout='wide')

# Title Dashboard
st.title('📊 Dashboard Analisis E-Commerce')
st.write('Analisis data e-commerce untuk mendapatkan wawasan dari penjualan dan pelanggan.')

# --- Pertanyaan 1: Kategori Produk Terlaris ---
st.subheader('🏆 10 Kategori Produk Terlaris')

produk_terlaris = data['product_category_name_english'].value_counts().head(10)

# Visualisasi dengan Matplotlib
fig1, ax1 = plt.subplots(figsize=(8, 6))
sns.barplot(x=produk_terlaris.index, y=produk_terlaris.values, ax=ax1, palette='viridis')
ax1.set_title('10 Kategori Produk Terlaris', fontsize=16)
ax1.set_xlabel('Kategori Produk', fontsize=12)
ax1.set_ylabel('Jumlah Pembelian', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
sns.despine(left=True, bottom=True)
st.pyplot(fig1)

# --- Pertanyaan 2: Metode Pembayaran Terpopuler ---
st.subheader('💳 Metode Pembayaran Terpopuler')

metode_pembayaran = data['payment_type'].value_counts()

# Visualisasi dengan Matplotlib
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.barplot(x=metode_pembayaran.index, y=metode_pembayaran.values, ax=ax2, palette='viridis')
ax2.set_title('Metode Pembayaran Terpopuler', fontsize=16)
ax2.set_xlabel('Metode Pembayaran', fontsize=12)
ax2.set_ylabel('Jumlah Transaksi', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
sns.despine(left=True, bottom=True)
st.pyplot(fig2)

# --- Pertanyaan 3: Kota dengan Jumlah Pelanggan Terbanyak ---
st.subheader('🏙️ 10 Kota dengan Jumlah Pelanggan Terbanyak')

city_customers = data['customer_city'].value_counts().head(10)

# Visualisasi dengan Matplotlib
fig3, ax3 = plt.subplots(figsize=(8, 6))
sns.barplot(x=city_customers.values, y=city_customers.index, ax=ax3, palette='viridis')
ax3.set_title('10 Kota dengan Pelanggan Terbanyak', fontsize=16)
ax3.set_xlabel('Jumlah Pelanggan', fontsize=12)
ax3.set_ylabel('Kota', fontsize=12)
sns.despine(left=True, bottom=True)
st.pyplot(fig3)

# Filter Berdasarkan Kota ---
st.subheader('🔎 Analisis Lebih Lanjut Berdasarkan Kota')

city_filter = st.selectbox('Pilih Kota untuk Analisis Lebih Lanjut:', data['customer_city'].unique())
filtered_data = data[data['customer_city'] == city_filter]

# Tampilkan Data Pelanggan Berdasarkan Kota yang Dipilih
st.subheader(f'📂 Data Pelanggan di {city_filter}')
st.dataframe(filtered_data)

# --- Kategori Produk Terlaris di Kota yang Dipilih ---
st.subheader(f'🏆 10 Kategori Produk Terlaris di {city_filter}')

if not filtered_data.empty:
    produk_terlaris_kota = filtered_data['product_category_name_english'].value_counts().head(10)
    
    # Visualisasi dengan Matplotlib
    fig4, ax4 = plt.subplots(figsize=(8, 6))
    sns.barplot(x=produk_terlaris_kota.index, y=produk_terlaris_kota.values, ax=ax4, palette='viridis')
    ax4.set_title(f'10 Kategori Produk Terlaris di {city_filter}', fontsize=16)
    ax4.set_xlabel('Kategori Produk', fontsize=12)
    ax4.set_ylabel('Jumlah Pembelian', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    sns.despine(left=True, bottom=True)
    st.pyplot(fig4)
else:
    st.warning(f'Tidak ada data untuk kota {city_filter}.')

# --- Penyesuaian Desain dan Warna ---
st.markdown("""
<style>
    .css-18e3th9 {
        padding: 2rem 1rem 2rem 1rem;
    }
    .css-1d391kg {
        text-align: center;
    }
    .stPlotlyChart {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 15px;
    }
</style>
""", unsafe_allow_html=True)
