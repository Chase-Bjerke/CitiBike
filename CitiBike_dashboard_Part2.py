################################################ CitiBike Strategy Dashboard ################################################

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from datetime import datetime as dt

################################################ Dashboard Setup ################################################

## Dashboard configuring
# ---------------------------------------------------------
st.set_page_config(page_title="CitiBike Strategy Dashboard", layout="wide")
st.title("CitiBike Strategy Dashboard")
st.markdown("This dashboard provides insights into NYC CitiBike usage patterns, "
    "popular stations, and the relationship between ridership and weather.")

# Sidebar navigation
page = st.sidebar.radio(
    "Navigate to:",
    ["Overview", "Daily Rides vs Weather", "Trip Duration", "Top Stations", "Trip Hotspots", "Recommendations"]
)

################################################ Import Prepared data ################################################
## Imports
# ---------------------------------------------------------
daily_df = pd.read_csv("02_Data/Prepared_Data/daily_sub_df.csv")

top_stations_df = pd.read_csv("02_Data/Prepared_Data/top_stations_df.csv")

################################################ DEFINE THE PAGES ################################################


################################################ CitiBike Strategy Overview Page ################################################

## Overview Page
# ---------------------------------------------------------
# Setup sidebar link
if page == "Overview":
    st.markdown("""

    need to write something
         
    This dashboard explores CitiBike usage patterns in NYC.
    We'll look at customer behavior, bike distribution, and opportunities
    for expansion to improve service and sustainability.



    """)


################################################ CitiBike NYC Daily Rides vs Temperature Chart ################################################

## Dual-Axis Chart
# ---------------------------------------------------------

# Setup sidebar link
elif page == "Daily Rides vs Weather":
    st.header("Daily Rides and Temperature Trends")

    # Insights of the chart
    # ---------------------------------------------------------
    st.markdown("""

    need to write something
     
     """)
    
    # Seasonal Filter (Note: This applies only to this chart.)
    # ---------------------------------------------------------
    st.sidebar.markdown("### Filter by Season")
    season_filter = st.sidebar.multiselect(
        label="Select season(s)",
        options=daily_df['season'].unique(),
        default=daily_df['season'].unique()
    )

    # Filter the dataframe based on user selection
    df_filtered = daily_df.query("season == @season_filter")
    
    # Plot Chart
    # ---------------------------------------------------------
    # Create a subplot with two y-axes
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add the daily bike rides line (left y-axis)
    fig.add_trace(
        go.Scatter(
            x=df_filtered["date"],
            y=df_filtered["bike_rides_daily"],
            name="Daily Bike Rides",
            line=dict(color="blue")
        ),
        secondary_y=False
    )

    # Add the average temperature line (right y-axis)
    fig.add_trace(
        go.Scatter(
            x=df_filtered["date"],
            y=df_filtered["avgTemp"],
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

################################################ CitiBike NYC: Trip Duration by Rider Type (1–65 Minutes) ################################################

## Box Plot
# ---------------------------------------------------------
# Setup sidebar link
elif page == "Trip Duration":
    st.header("Trip Duration by Rider Type")

    # Insights of the chart
    # ---------------------------------------------------------
    st.markdown("""

    Need to write something
     
         """)

    # Display Box Plot chart image
    # ---------------------------------------------------------
    st.image("04_Analysis/Visualizations/tripduration_boxplot_static.png", use_container_width=True)

################################################ CitiBike NYC Top Stations Chart ################################################

## Bar Chart
# ---------------------------------------------------------
# Setup sidebar link 
elif page == "Top Stations":
    st.header("Top 20 Most Popular CitiBike Stations in NYC")

    # Insights of the chart
    # ---------------------------------------------------------
    st.markdown("""

    Need to write something
     
         """)

    # Sort ascending for horizontal bars
    top20 = top_stations_df.sort_values("value", ascending=True)

    # Plot chart
    # ---------------------------------------------------------
    fig = go.Figure(go.Bar(
        x=top20["value"],
        y=top20["start_station_name"],
        orientation="h",
        marker=dict(
            color=top20["value"],
            colorscale="Blues"
        )
    ))

    fig.update_layout(
        title="Top 20 Most Popular CitiBike Stations in NYC",
        xaxis_title="Ride Count",
        yaxis_title="Station Name",
        template="plotly_white",
        height=600
    )

    # Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)

################################################ CitiBike NYC Trip Hotspots (500 Busiest Routes) ################################################

## Trip Flow Map
# ---------------------------------------------------------
# Setup sidebar link
elif page == "Trip Hotspots":
    st.subheader("NYC CitiBike – Top 500 Trip Flows")

    # Insights of the chart
    # ---------------------------------------------------------
    st.markdown("""

    Need to write something
     
         """)

    st.subheader("NYC CitiBike – Top 500 Trip Flows")

    path_to_html = "02_Data/Prepared_Data/kepler.gl.html"


    # Read file and keep in variable
    # ---------------------------------------------------------
    with open(path_to_html, 'r') as f:
        html_data = f.read()

    # Show in webpage
    st.components.v1.html(html_data, height=1000)

################################################ Recommendations Page ################################################

## Recommendations Page
# ---------------------------------------------------------
# Setup sidebar link
elif page == "Recommendations":
    st.header("Recommendations")

    ### Insights of the chart
    st.markdown("""

    Need to write something
     
         """)