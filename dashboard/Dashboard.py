import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

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
fig1 = px.bar(produk_terlaris, x=produk_terlaris.index, y=produk_terlaris.values, 
              labels={'x':'Kategori Produk', 'y':'Jumlah Pembelian'},
              color=produk_terlaris.index, 
              color_discrete_sequence=px.colors.sequential.Viridis,
              title='10 Kategori Produk Terlaris')
fig1.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig1)

# --- Pertanyaan 2: Metode Pembayaran Terpopuler ---
st.subheader('💳 Metode Pembayaran Terpopuler')

metode_pembayaran = data['payment_type'].value_counts()
fig2 = px.pie(metode_pembayaran, values=metode_pembayaran.values, names=metode_pembayaran.index, 
              title='Proporsi Metode Pembayaran',
              color_discrete_sequence=px.colors.sequential.Viridis)
fig2.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig2)

# --- Pertanyaan 3: Kota dengan Jumlah Pelanggan Terbanyak ---
st.subheader('🏙️ 10 Kota dengan Jumlah Pelanggan Terbanyak')

city_customers = data['customer_city'].value_counts().head(10)
fig3 = px.bar(city_customers, x=city_customers.values, y=city_customers.index, 
              labels={'x':'Jumlah Pelanggan', 'y':'Kota'},
              color=city_customers.index, 
              color_discrete_sequence=px.colors.sequential.Viridis,
              title='10 Kota dengan Pelanggan Terbanyak',
              orientation='h')
st.plotly_chart(fig3)

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
    fig4 = px.bar(produk_terlaris_kota, x=produk_terlaris_kota.index, y=produk_terlaris_kota.values, 
                  labels={'x':'Kategori Produk', 'y':'Jumlah Pembelian'},
                  color=produk_terlaris_kota.index, 
                  color_discrete_sequence=px.colors.sequential.Viridis,
                  title=f'10 Kategori Produk Terlaris di {city_filter}')
    fig4.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig4)
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
</style>
""", unsafe_allow_html=True)
