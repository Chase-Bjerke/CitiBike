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
if page == "Overview":

    # -------------------------------
    # Centered Title
    # -------------------------------
    st.markdown(
        "<h2 style='text-align:center;'>CitiBike Strategy Dashboard</h2>",
        unsafe_allow_html=True
    )

    # -------------------------------
    # Centered, tight intro paragraph
    # -------------------------------
    intro_left, intro_center, intro_right = st.columns([1, 2, 1])
    with intro_center:
        st.markdown("""
This dashboard provides a descriptive analysis of New York City’s Citi Bike system, enabling the business strategy team to understand current usage patterns and identify opportunities to enhance bike availability throughout the city.
""")

    # -------------------------------
    # Centered image below intro
    # -------------------------------
    st.markdown(
        "<div style='text-align:center; margin-top:10px; margin-bottom:20px;'>",
        unsafe_allow_html=True
    )
    st.image(
        "04_Analysis/Visualizations/green_light_bike.jpg",
        width=420   # increased size
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------
    # Two-column main content
    # Right column widened for readability
    # -------------------------------
    col_left, col_right = st.columns([1, 1.3])

    with col_left:
        st.markdown("""
### Project Objective
As the lead analyst, the goal is to identify where distribution issues originate and provide actionable insights that support informed operational decision-making. The analysis focuses on understanding whether availability problems stem from:
- uneven station demand  
- weather-driven fluctuations  
- trip behavior  
- geographic hotspots  
- or a combination of these factors  

Understanding these patterns is essential for improving system reliability and ensuring riders can consistently find and return bikes across the city.
""")

    with col_right:
        st.markdown("""
### What This Dashboard Covers
The analysis is organized into several pages, each focusing on a key aspect of system performance:

- **Most Popular Stations**  
  Identifies high‑demand hubs and highlights where capacity is consistently strained.

- **Weather and Daily Rides**  
  Examines how temperature and conditions influence daily trip volume.

- **Trip Duration Patterns**  
  Explores how long riders typically travel and what that reveals about user behavior.

- **Geographic Hotspots**  
  Maps where trips cluster across the city to reveal spatial demand patterns.

- **Recommendations**  
  Summarizes opportunities to improve distribution, expand capacity, and support future growth.

Use the **Navigate to** in the sidebar to move between sections.
""")
 
################################################ CitiBike NYC Daily Rides vs Temperature Chart ################################################

## Dual-Axis Chart
# ---------------------------------------------------------

# Setup sidebar link
elif page == "Daily Rides vs Weather":
    st.header("Daily Rides and Temperature Trends")

    st.markdown("""
    need to write something
    """)

    # Seasonal Filter (Note: This applies only to this chart.)
    # ---------------------------------------------------------
    season_options = ["All"] + list(daily_df['season'].unique())

    st.sidebar.markdown("### Filter by Season")
    season_filter = st.sidebar.multiselect(
        label="Select season(s)",
        options=season_options,
        default=["All"]
    )

    # Filter logic
    if "All" in season_filter:
        df_filtered = daily_df
    else:
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