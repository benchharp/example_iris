import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Iris Dashboard", layout="wide")

st.title("🌸 Iris Flower Data Dashboard")

# Load the Iris dataset
df = px.data.iris()

# Sidebar filters
species = st.sidebar.multiselect("Select Species", df["species"].unique(), default=df["species"].unique())

# Filter data
filtered_df = df[df["species"].isin(species)]

# Plot 1: Scatter Plot
st.subheader("Sepal Dimensions")
fig1 = px.scatter(
    filtered_df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)
st.plotly_chart(fig1, use_container_width=True)

# Plot 2: Box Plot
st.subheader("Petal Length Distribution")
fig2 = px.box(
    filtered_df,
    x="species",
    y="petal_length",
    color="species"
)
st.plotly_chart(fig2, use_container_width=True)
