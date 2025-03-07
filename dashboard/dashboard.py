import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load dataset
df = pd.read_csv("dashboard/main_data.csv")

# Hitung jumlah pelanggan per kota
city_distribution = df["customer_city"].value_counts().reset_index()
city_distribution.columns = ["customer_city", "count"]

# Hitung jumlah pelanggan per negara bagian
state_distribution = df["customer_state"].value_counts().reset_index()
state_distribution.columns = ["customer_state", "count"]

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")


# Streamlit dashboard
st.title("Dashboard Analisis Pelanggan")

st.subheader("Kota dengan Pelanggan Terbanyak")

most_populous_city = city_distribution.iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.metric("City", value=most_populous_city["customer_city"])

with col2:
    st.metric("Total customers", value=most_populous_city["count"])

# Visualisasi kota dengan pelanggan terbanyak
st.subheader("10 Kota dengan Pelanggan Terbanyak")
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(
    city_distribution["customer_city"][:10],
    city_distribution["count"][:10],
    color="purple",
)
ax.set_xlabel("City")
ax.set_ylabel("Number of Customers")
ax.set_title("10 Cities with the Most Customers")
ax.set_xticklabels(city_distribution["customer_city"][:10], rotation=45)

# Menambahkan jumlah pelanggan di atas tiap bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(int(height)),
        ha="center",
        va="bottom",
    )

st.pyplot(fig)

st.subheader("Negara Bagian dengan Pelanggan Terbanyak")

# Negara bagian dengan jumlah pelanggan terbanyak
most_populous_state = state_distribution.iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.metric("State", value=most_populous_state["customer_state"])

with col2:
    st.metric("Total customers", value=most_populous_state["count"])

# Visualisasi 10 negara bagian dengan pelanggan terbanyak
st.subheader("10 Negara Bagian dengan Pelanggan Terbanyak")
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(
    state_distribution["customer_state"][:10],
    state_distribution["count"][:10],
    color="blue",
)
ax.set_xlabel("State")
ax.set_ylabel("Number of Customers")
ax.set_title("Top 10 State with the Most Customers")
ax.set_xticklabels(state_distribution["customer_state"], rotation=45)

# Menambahkan jumlah pelanggan di atas tiap bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(int(height)),
        ha="center",
        va="bottom",
    )

st.pyplot(fig)


# Clustering dengan teknik Binning
st.title("Clustering dengan teknik Binning")

# Clustering dengan teknik Binning untuk kota
bin_edges = np.linspace(
    city_distribution["count"].min(), city_distribution["count"].max(), num=4
)
labels = ["Low", "Medium", "High"]
city_distribution["bin_category"] = pd.cut(
    city_distribution["count"], bins=bin_edges, labels=labels, include_lowest=True
)

# Mengambil top 10 data dan reset index
top_cities = city_distribution.head(10).copy().reset_index(drop=True)

# Streamlit App
st.subheader("Clustering Kota dengan Teknik Binning")

# Plot hasil clustering
st.subheader("Top 10 Cities - Count with Binning Categories")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(
    x="customer_city",
    y="count",
    hue="bin_category",
    data=top_cities,
    palette="viridis",
    ax=ax1,
)
plt.xticks(rotation=45)
plt.xlabel("City")
plt.ylabel("Customers Count")
plt.title("Top 10 Cities - Count with Binning Categories")
st.pyplot(fig1)

# Visualisasi distribusi pelanggan berdasarkan binning kategori kota
st.subheader("Distribusi Kota Berdasarkan Kategori Pelanggan")
bin_counts = city_distribution["bin_category"].value_counts().sort_index()

fig2, ax2 = plt.subplots(figsize=(8, 5))
bars = ax2.bar(
    bin_counts.index, bin_counts.values, color=["#2F3E58", "#008080", "lightgreen"]
)
ax2.set_xlabel("Category")
ax2.set_ylabel("Number of Cities")
ax2.set_title("City Distribution by Binned Customer Count")

# Menambahkan jumlah data di atas tiap bar
for bar in bars:
    height = bar.get_height()
    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(int(height)),
        ha="center",
        va="bottom",
    )

st.pyplot(fig2)

# Clustering dengan teknik Binning untuk negara bagian
bin_edges_state = np.linspace(
    state_distribution["count"].min(), state_distribution["count"].max(), num=4
)
state_distribution["bin_category"] = pd.cut(
    state_distribution["count"],
    bins=bin_edges_state,
    labels=labels,
    include_lowest=True,
)


# Mengambil top 10 data dan reset index
top_state = state_distribution.head(10).copy().reset_index(drop=True)

# Streamlit App
st.subheader("Clustering Negara Bagian dengan Teknik Binning")

# Plot hasil clustering
st.subheader("Top 10 State - Count with Binning Categories")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(
    x="customer_state",
    y="count",
    hue="bin_category",
    data=top_state,
    palette="viridis",
    ax=ax1,
)
plt.xticks(rotation=45)
plt.xlabel("City")
plt.ylabel("Customers Count")
plt.title("Top 10 State - Count with Binning Categories")
st.pyplot(fig1)

# Visualisasi distribusi pelanggan berdasarkan binning kategori negara bagian
st.subheader("Distribusi Negara Bagian Berdasarkan Kategori Pelanggan")
bin_edges_state = state_distribution["bin_category"].value_counts().sort_index()
num_bins = len(bin_edges_state)
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(
    bin_edges_state.index,
    bin_edges_state.values,
    color=["#2F3E58", "teal", "lightgreen"][:num_bins],
)
ax.set_xlabel("Category")
ax.set_ylabel("Number of Cities")
ax.set_title("City Distribution by Binned Customer Count")

# Menambahkan jumlah data di atas tiap bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(int(height)),
        ha="center",
        va="bottom",
    )

st.pyplot(fig)
