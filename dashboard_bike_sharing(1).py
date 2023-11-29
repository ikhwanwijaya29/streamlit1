#Nama       : Ikhlasul Ikhwan Wijaya
#Email      : ikhwanwijaya76@gmail.com
#Dicoding   : https://www.dicoding.com/users/ikhwan29/

#Import Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==============================
# LOAD DATA
# ==============================

@st.cache_resource
def load_data():
    data = pd.read_csv("../dataset/Bike-sharing-dataset/hour.csv")
    return data

data = load_data()

# ==============================
# DASHBOARD TITLE
# ==============================
# Set page title
st.title("Bike Share Dashboard")

# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("Information:")
st.sidebar.markdown("**• Author: Ikhwan Wijaya**")
st.sidebar.markdown(
    "**• Email: [ikhwanwijaya76@gmail.com](ikhwanwijaya76@gmail.com)**")
st.sidebar.markdown(
    "**• Dicoding: [maulanakavaldo](https://www.dicoding.com/users/ikhwan29/)**")

st.sidebar.title("Bike Share Dataset")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Show dataset source
st.sidebar.markdown("[Download Dataset](https://link-to-your-dataset)")

st.sidebar.markdown('**Weather:**')
st.sidebar.markdown('1: Clear, Few clouds, Partly cloudy, Partly cloudy')
st.sidebar.markdown('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
st.sidebar.markdown('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
st.sidebar.markdown('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')

# ==============================
# VISUALIZATION
# ==============================
# create a layout with two columns
col1, col2 = st.columns(2)

with col1:
    # Season-wise bike share count
    season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
    data["season_label"] = data["season"].map(season_mapping)
    season_count = data.groupby("season_label")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="season_label",
                              y="cnt", title="Season-wise Bike Share Count")
    st.plotly_chart(fig_season_count, use_container_width=True,
                    height=400, width=600)

with col2:
    # Weather situation-wise bike share count
    weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weathersit",
                               y="cnt", title="Weather Situation-wise Bike Share Count")
    st.plotly_chart(fig_weather_count, use_container_width=True,height=400, width=800)

# Hourly bike share count
hourly_count = data.groupby("hr")["cnt"].sum().reset_index()
fig_hourly_count = px.line(
    hourly_count, x="hr", y="cnt", title="Hourly Bike Share Count")
st.plotly_chart(fig_hourly_count, use_container_width=True,
                height=400, width=600)

# Humidity vs. Bike Share Count
fig_humidity_chart = px.scatter(
    data, x="hum", y="cnt", title="Humidity vs. Bike Share Count")
st.plotly_chart(fig_humidity_chart)

# Wind Speed vs. Bike Share Count
fig_wind_speed_chart = px.scatter(
    data, x="windspeed", y="cnt", title="Wind Speed vs. Bike Share Count")
st.plotly_chart(fig_wind_speed_chart)

# Temperature vs. Bike Share Count
fig_temp_chart = px.scatter(data, x="temp", y="cnt",
                            title="Temperature vs. Bike Share Count")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=400, width=800)

# Show data source and description
st.sidebar.title("About")
st.sidebar.info("This dashboard displays visual")
