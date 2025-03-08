import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load dataset
df = pd.read_csv("main_data.csv")

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

# fitur interaktif - Slider untuk memilih jumlah kota teratas
top_n_cities = st.slider("Pilih jumlah kota teratas untuk ditampilkan:", 5, 20, 10)

# Update visualisasi kota dengan pelanggan terbanyak
st.subheader(f"{top_n_cities} Kota dengan Pelanggan Terbanyak")
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(
    city_distribution["customer_city"][:top_n_cities],
    city_distribution["count"][:top_n_cities],
    color="lightblue",
)
ax.set_xlabel("City")
ax.set_ylabel("Number of Customers")
ax.set_title(f"Top {top_n_cities} Cities with the Most Customers")
ax.set_xticklabels(city_distribution["customer_city"][:top_n_cities], rotation=45)

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

# fitur interaktif - Slider untuk memilih jumlah negara bagian teratas
top_n_states = st.slider("Pilih jumlah negara bagian teratas untuk ditampilkan:", 5, 20, 10)

# Update visualisasi negara bagian dengan pelanggan terbanyak
st.subheader(f"{top_n_states} Negara Bagian dengan Pelanggan Terbanyak")
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(
    state_distribution["customer_state"][:top_n_states],
    state_distribution["count"][:top_n_states],
    color="lightblue",
)
ax.set_xlabel("State")
ax.set_ylabel("Number of Customers")
ax.set_title(f"Top {top_n_states} States with the Most Customers")
ax.set_xticklabels(state_distribution["customer_state"][:top_n_states], rotation=45)

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
st.title("Clustering Kota dengan Teknik Binning")

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
st.title("Clustering Negara Bagian dengan Teknik Binning")

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

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(
    bin_edges_state.index,
    bin_edges_state.values,
    color=["#2F3E58", "teal", "lightgreen"],
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
