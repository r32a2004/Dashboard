import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set title in the navbar
st.set_page_config(page_title="Analisis Udara", layout="wide")

# Navbar with title
st.markdown("<h1 style='text-align: center;'>Analisis Udara</h1>", unsafe_allow_html=True)

# Sidebar with menu
st.sidebar.title("Menu")

menu = st.sidebar.radio(
    "Pilih Halaman:",
    ('Dashboard', 'Analisis Lanjutan')
)

# Dashboard page
if menu == 'Dashboard':
    st.write(
        """
        # Dashboard
        Selamat datang di halaman dashboard. 
        Di sini kita akan menampilkan informasi penting terkait analisis udara.
        """
    )
   
    data = pd.read_csv('data_bersih.csv')
    grupPM10ByMonth = data.groupby(['year','month'])['PM10'].sum()
    grupCOyMonthYears = data.groupby(['year','month'])['CO'].sum()
    grupNOByMonthYears = data.groupby(['month','year'])['NO2'].sum()
    grupO3MonthYears = data.groupby(['year','month'])['O3'].sum()
    max_coYear=data.groupby(['year'])['CO'].max()
    min_coYear=data.groupby(['year'])['CO'].min()
    max_no_year=data.groupby(['year'])['NO2'].max()
    min_no_year=data.groupby(['year'])['NO2'].min()
    max_soyear=data.groupby(['year'])['SO2'].max()
    min_soyear=data.groupby(['year'])['SO2'].min()

    grupPM25ByMonth = data.groupby(['year','month'])['PM2.5'].sum()
    max_pm2year=data.groupby(['year'])['PM2.5'].max()
    min_pm2year=data.groupby(['year'])['PM2.5'].min()
    max_pm10year=data.groupby(['year'])['PM10'].max()
    min_pm10year=data.groupby(['year'])['PM10'].min()
    df = grupPM25ByMonth.reset_index()
    grupCOyear = data.groupby(['year'])['CO'].sum()
    grupNOyear = data.groupby(['year'])['NO2'].sum()
    grupSOyear = data.groupby(['year'])['SO2'].sum()
    gruppm10year = data.groupby(['year'])['PM10'].sum()


    heatmap_data = df.pivot_table(index='year', columns='month', values='PM2.5', aggfunc='sum')
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.1f', linewidths=.5)
    plt.title('Heatmap Jumlah Partikel PM2.5 Berdasarkan Bulan dan Tahun')
    plt.xlabel('Bulan')
    plt.ylabel('Tahun')
    st.pyplot(plt)

    df_grupPM10ByMonth = grupPM10ByMonth.reset_index()
    heatmap_data_grupPM10ByMonth = df_grupPM10ByMonth.pivot_table(index='year', columns='month', values='PM10', aggfunc='sum')
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data_grupPM10ByMonth, cmap='YlGnBu', annot=True, fmt='.1f', linewidths=.5)
    plt.title('Heatmap Jumlah Partikel PM10 Bulan bedasrkan setiap Tahun')
    plt.xlabel('Bulan')
    plt.ylabel('Tahun')
    st.pyplot(plt)
    df = grupCOyMonthYears.reset_index()
    heatmap_data = df.pivot_table(index='year', columns='month', values='CO', aggfunc='sum')
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.1f', linewidths=.5)
    plt.title('Heatmap Jumlah Partikel CO Bulan bedasrkan setiap Tahun')
    plt.xlabel('Bulan')
    st.pyplot(plt)
    df = grupO3MonthYears.reset_index()
    heatmap_data = df.pivot_table(index='year', columns='month', values='O3', aggfunc='sum')
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.1f', linewidths=.5)
    plt.title('Heatmap Jumlah Partikel O3 Bulan bedasrkan setiap Tahun')
    plt.xlabel('Bulan')
    plt.ylabel('Tahun')
    st.pyplot(plt)
    df =grupNOByMonthYears.reset_index()
    heatmap_data = df.pivot_table(index='year', columns='month', values='NO2', aggfunc='sum')
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.1f', linewidths=.5)
    plt.title('Heatmap Jumlah Partikel NO2 Bulan bedasrkan setiap Tahun')
    plt.xlabel('Bulan')
    plt.ylabel('Tahun')
    st.pyplot(plt)
    st.write(
        """
        # CO Maksimum Dan Minimum per tahun
        """
    )
    
    col1, col2 = st.columns(2)
    with col1:
        plt.figure(figsize=(12, 6))
        bars_max = plt.bar(max_coYear.index, max_coYear.values, color='red', alpha=0.7, label='Maksimum CO')
        plt.title('CO Maksimum per Tahun')
        plt.xlabel('Tahun')
        plt.ylabel('CO')
        plt.legend()
        plt.grid(True)

        # Menampilkan nilai di atas batang
        for bar in bars_max:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 1), va='bottom')
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        st.pyplot(plt)

    # Plot untuk CO Minimum per Tahun di kolom kedua
    with col2:
        plt.figure(figsize=(12, 6))
        bars_min = plt.bar(min_coYear.index, min_coYear.values, color='blue', alpha=0.7, label='Minimum CO')
        plt.title('CO Minimum per Tahun')
        plt.xlabel('Tahun')
        plt.ylabel('CO')
        plt.legend()
        plt.grid(True)

        # Menampilkan nilai di atas batang
        for bar in bars_min:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 1), va='bottom')

        st.pyplot(plt)
    st.write(
        """
        # NO2 Maksimum Dan Minimum per tahun
        """
    )
    col1, col2 = st.columns(2)
    with col1:
        plt.figure(figsize=(12, 6))
        bars_max = plt.bar(max_no_year.index, max_no_year.values, color='red', alpha=0.7, label='Maksimum NO2')
        plt.title('NO2 Maksimum per Tahun')
        plt.xlabel('Tahun')
        plt.ylabel('NO2')
        plt.legend()
        plt.grid(True)
        for bar in bars_max:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 1), va='bottom')
        st.pyplot(plt)
    # Plot untuk CO Minimum per Tahun di kolom kedua
    with col2:
        plt.figure(figsize=(12, 6))
        bars_min = plt.bar(min_no_year.index, min_no_year.values, color='blue', alpha=0.7, label='Minimum NO2')
        plt.title('NO2 Minimum per Tahun')
        plt.xlabel('Tahun')
        plt.ylabel('NO2')
        plt.legend()
        plt.grid(True)
        for bar in bars_min:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 1), va='bottom')
        st.pyplot(plt)
    st.write(
        """
        # SO2 Maksimum Dan Minimum per tahun
        """
    )
    col1, col2 = st.columns(2)
    with col1:
        plt.figure(figsize=(12, 6))
        bars_max = plt.bar(max_soyear.index, max_soyear.values, color='red', alpha=0.7, label='Maksimum SO2')
        plt.title('SO2 Maksimum per Tahun')
        plt.xlabel('Tahun')
        plt.ylabel('SO2')
        plt.legend()
        plt.grid(True)
        for bar in bars_max:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 1), va='bottom')
        st.pyplot(plt)

    with col2:
        plt.figure(figsize=(12, 6))
        bars_min = plt.bar(min_soyear.index, min_soyear.values, color='blue', alpha=0.7, label='Minimum SO2')
        plt.title('SO2 Minimum per Tahun')
        plt.xlabel('Tahun')
        plt.ylabel('SO2')
        plt.legend()
        plt.grid(True)
        for bar in bars_min:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 1), va='bottom')
        st.pyplot(plt)
    st.write(
        """
        # PM2.5 Maksimum Dan Minimum per tahun
        """
    )
    col1, col2 = st.columns(2)
    with col1:
    
        plt.figure(figsize=(12, 6))
        bars_max = plt.bar(max_pm2year.index, max_pm2year.values, color='red', alpha=0.7, label='Maksimum PM2.5')
        plt.title('Pm2.5 Maksimum per Tahun')
        plt.xlabel('Tahun')
        plt.ylabel('Pm2.5')
        plt.legend()
        plt.grid(True)
        for bar in bars_max:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 1), va='bottom')
        st.pyplot(plt)

    with col2:
        plt.figure(figsize=(12, 6))
        bars_min = plt.bar(max_pm2year.index, max_pm2year.values, color='blue', alpha=0.7, label='Minimum PM2.5')
        plt.title('PM2.5 Minimum per Tahun')
        plt.xlabel('Tahun')
        plt.ylabel('PM2.5')
        plt.legend()
        plt.grid(True)
        for bar in bars_min:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 1), va='bottom')
        st.pyplot(plt)
    st.write(
        """
        # PM10  Maksimum Dan Minimum per tahun
        """
    )
    col1, col2 = st.columns(2)
    bars_max = plt.bar(max_pm10year.index, max_pm10year.values, color='red', alpha=0.7, label='Maksimum PM10')
    plt.title('Pm10 Maksimum per Tahun')
    plt.xlabel('Tahun')
    plt.ylabel('Pm10')
    plt.legend()
    plt.grid(True)
    for bar in bars_max:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 1), va='bottom')
    st.pyplot(plt)
    plt.figure(figsize=(12, 6))
    bars_min = plt.bar(max_pm10year.index, max_pm10year.values, color='blue', alpha=0.7, label='Minimum PM10')
    plt.title('PM10 Minimum per Tahun')
    plt.xlabel('Tahun')
    plt.ylabel('PM2.5')
    plt.legend()
    plt.grid(True)
    for bar in bars_min:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 1), va='bottom')
    st.pyplot(plt)
    plt.figure(figsize=(10, 7))
    plt.pie(grupCOyear,
        labels=grupCOyear.index,
        autopct=lambda p: '{:.0f}'.format(p * sum(grupCOyear) / 100),
        colors=plt.cm.Paired(range(len(grupCOyear))),  #
        startangle=140,
        shadow=True)
    plt.title('Distribusi CO per Tahun')
    plt.axis('equal')
    st.pyplot(plt)
    

    plt.figure(figsize=(10, 7))
    plt.pie(grupNOyear,
        labels=grupCOyear.index,
        autopct=lambda p: '{:.0f}'.format(p * sum(grupNOyear) / 100),
        colors=plt.cm.Paired(range(len(grupNOyear))),  #
        startangle=140,
        shadow=True)
    plt.title('Distribusi NO2 per Tahun')
    plt.axis('equal')
    st.pyplot(plt)


    plt.figure(figsize=(10, 7))
    plt.pie(grupSOyear,
        labels=grupSOyear.index,
        autopct=lambda p: '{:.0f}'.format(p * sum(grupSOyear) / 100),
        colors=plt.cm.Paired(range(len(grupSOyear))),  #
        startangle=140,
        shadow=True)
    plt.title('Distribusi SO2 per Tahun')
    plt.axis('equal')
    st.pyplot(plt)
    

    plt.figure(figsize=(10, 7))
    plt.pie(gruppm10year,
        labels=gruppm10year.index,
        autopct=lambda p: '{:.0f}'.format(p * sum(gruppm10year) / 100),
        colors=plt.cm.Paired(range(len(gruppm10year))),  #
        startangle=140,
        shadow=True)
    plt.title('Distribusi PM10 per Tahun')
    plt.axis('equal')
    st.pyplot(plt)



   






# Analisis Lanjutan page
elif menu == 'Analisis Lanjutan':
    data = pd.read_csv('data_bersih.csv')
    st.write(
        """
        # Analisis Lanjutan
        Ini Jumlah Udara yang Baik
        """


    )
    count_baik_per_bulan = data[data['Kualitas_Udara'] == ' Baik'].groupby(['year', 'month']).size().reset_index(name='Jumlah_Baik')
    heatmap_data = count_baik_per_bulan.pivot_table(index='year', columns='month', values='Jumlah_Baik')
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='g', linewidths=.5)
    plt.title('Heatmap Jumlah udara yang bersih ')
    plt.xlabel('Bulan')
    plt.ylabel('Tahun')
    st.pyplot(plt)

    
