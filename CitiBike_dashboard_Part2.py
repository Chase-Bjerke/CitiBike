################################################ CitiBike Strategy Dashboard #####################################################

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from datetime import datetime as dt

########################### Dashboard Setup ##################################################################

st.set_page_config(page_title="CitiBike Strategy Dashboard", layout="wide")
st.title("CitiBike Strategy Dashboard")
st.markdown("This dashboard provides insights into NYC CitiBike usage patterns, "
    "popular stations, and the relationship between ridership and weather.") 

########################## Import Prepared data ###########################################################################################

daily_df = pd.read_csv("02_Data/Prepared_Data/daily_sub_df.csv")
top_stations_df = pd.read_csv("02_Data/Prepared_Data/top_stations_df.csv")

########################################### Top Stations Chart #####################################################################

## Bar Chart

fig = go.Figure(go.Bar(
    x=top_stations_df["start_station_name"],
    y=top_stations_df["value"],
    marker=dict(
        color=top_stations_df["value"],
        colorscale="Blues",
        reversescale=False
    )
))

fig.update_layout(
    title="Top 20 Most Popular CitiBike Stations in NYC",
    xaxis_title="Station Name",
    yaxis_title="Ride Count",
    width=900,
    height=600,
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

###########################################  Daily Rides vs Temperature Chart
####################################################################

## Dual-Axis Chart

st.header("Daily Rides and Temperature Trends")

# Create subplot with two y-axes
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add the daily bike rides line (left y-axis)
fig.add_trace(
    go.Scatter(
        x=daily_df["date"],
        y=daily_df["bike_rides_daily"],
        name="Daily Bike Rides",
        line=dict(color="blue")
    ),
    secondary_y=False
)

# Add the average temperature line (right y-axis)
fig.add_trace(
    go.Scatter(
        x=daily_df["date"],
        y=daily_df["avgTemp"],
        name="Average Temperature (°F)",
        line=dict(color="orange")
    ),
    secondary_y=True
)

# Update layout
fig.update_layout(
    title="Daily CitiBike Rides and Temperature in NYC (2022)",
    xaxis_title="Date",
    template="plotly_white",
    height=600,
    width=1000,
    legend_title="Metrics"
)

# Label the y-axes
fig.update_yaxes(title_text="Daily Bike Rides", secondary_y=False)
fig.update_yaxes(title_text="Temperature (°F)", secondary_y=True)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

###########################################  NYC CitiBike Trip Hotspots (500 Busiest Routes)
####################################################################

## Trip Flow Map

st.subheader("NYC CitiBike – Top 500 Trip Flows")

path_to_html = "02_Data/Prepared_Data/kepler.gl.html"


# Read file and keep in variable
with open(path_to_html, 'r') as f:
    html_data = f.read()

## Show in webpage
st.components.v1.html(html_data, height=1000)

###########################################  NYC CitiBike Trip Duration (Filtered to ~1–65 Minutes)
####################################################################

# Sample of data
sample = tripdur_focus.sample(n=500000

                              # Box plot

fig = px.box(
    sample,
    x="member_casual",
    y="tripduration",
    color="member_casual",
    points="outliers",
    color_discrete_sequence=["blue", "orange"],
    title="Trip Duration (Filtered to ~1–65 Minutes)"
)

fig.update_layout(
    xaxis_title="User Type",
    yaxis_title="Trip Duration (minutes)",
    showlegend=False,
    height=500,
    width=900
)

st.plotly_chart(fig, use_container_width=True)
