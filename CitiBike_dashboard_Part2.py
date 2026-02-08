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

    # --------------------------------
    # TITLE
    # --------------------------------
    title_left, title_center, title_right = st.columns([0.38, 1, 0.62])
    with title_center:
        st.markdown(
            """
            <h1 style='
                text-align:center;
                font-size:46px;
                margin-top:0px;
                margin-bottom:10px;
            '>
                CitiBike Strategy Dashboard
            </h1>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------
    # IMAGE
    # --------------------------------
    img_left, img_center, img_right = st.columns([1, 2, 1])
    with img_center:
        st.markdown(
            """
            <div style='
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 5px;
                margin-bottom: 15px;
            '>
            """,
            unsafe_allow_html=True
        )
        st.image("04_Analysis/Visualizations/green_light_bike.jpg", width=450)
        st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------
    # INTRO 
    # --------------------------------
    intro_left, intro_center, intro_right = st.columns([0.18, 1.65, 0.17])
    with intro_center:
        st.markdown("""
This dashboard provides a descriptive analysis of New York City’s Citi Bike system, enabling the business strategy team to understand current usage patterns and identify opportunities to enhance bike availability throughout the city.
""")

    # --------------------------------
    # TWO-COLUMN MAIN CONTENT
    # --------------------------------
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

# ---------------------------------------------------------
## Dual-Axis Chart
# ---------------------------------------------------------

# Setup sidebar link
elif page == "Daily Rides vs Weather":

    # --------------------------------
    # TITLE (matches Overview styling)
    # --------------------------------
    title_left, title_center, title_right = st.columns([0.38, 1, 0.62])
    with title_center:
        st.markdown(
            """
            <h1 style='
                text-align:center;
                font-size:46px;
                margin-top:0px;
                margin-bottom:10px;
            '>
                Daily Rides vs Weather
            </h1>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------
    # INSIGHTS
    # --------------------------------
    st.markdown("""

    The dual‑axis chart below shows a strong seasonal relationship between temperature and Citi Bike ridership. 
    Warmer days consistently have higher ride volume, while colder seasons see a predictable decline. This pattern 
    is especially visible from March through September, when rising temperatures coincide with a steady increase 
    in daily rides.

    CitiBike's peak ridership occurs during the late summer and early fall, with September showing both some of 
    the highest daily peaks and some unusually low days, suggesting weather patterns are unpredictable during 
    this time. As temperatures fall and daylight decreases in November, daily ridership drops sharply, reflecting 
    the seasonal shift toward colder, shorter, and more unpredictable days.

    Overall, the chart highlights a clear correlation: as temperatures rise, ridership increases, and as temperatures 
    fall, ridership declines. This seasonal pattern is a crucial variable in understanding CitiBike's demand and 
    planning bike availability throughout the year.
    """)

    # ---------------------------------------------------------
    # Seasonal Filter
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

    # ---------------------------------------------------------
    # Plot Chart
    # ---------------------------------------------------------
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(
            x=df_filtered["date"],
            y=df_filtered["bike_rides_daily"],
            name="Daily Bike Rides",
            line=dict(color="blue")
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=df_filtered["date"],
            y=df_filtered["avgTemp"],
            name="Average Temperature (°F)",
            line=dict(color="orange")
        ),
        secondary_y=True
    )

    fig.update_layout(
        title="Daily CitiBike Rides and Temperature in NYC (2022)",
        xaxis_title="Date",
        template="plotly_white",
        height=600,
        width=1000,
        legend_title="Metrics"
    )

    fig.update_yaxes(title_text="Daily Bike Rides", secondary_y=False)
    fig.update_yaxes(title_text="Temperature (°F)", secondary_y=True)

    st.plotly_chart(fig, use_container_width=True)

    

################################################ CitiBike NYC: Trip Duration by Rider Type (1–65 Minutes) ################################################

## Box Plot
# ---------------------------------------------------------
elif page == "Trip Duration":

    # --------------------------------
    # TITLE
    # --------------------------------
    title_left, title_center, title_right = st.columns([0.38, 1, 0.62])
    with title_center:
        st.markdown(
            """
            <h1 style='
                text-align:center;
                font-size:46px;
                margin-top:0px;
                margin-bottom:10px;
            '>
                CitiBike NYC — Trip Duration by Rider Type
            </h1>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------
    # KEY INSIGHTS
    # --------------------------------
    st.markdown("""

    Trip duration provides a clear look into CitiBike’s customer behavior and how different rider groups use the system. 
    From the box plot, there is an immediate distinction between Member and Casual riders. Members tend to take shorter, 
    more consistent trips that align with routine, purpose‑driven travel. Casual riders, on the other hand, take longer 
    and more variable trips, reflecting leisure‑oriented behavior and more flexible travel patterns.

    These differences help clarify how each group engages with the system and what types of trips they rely on CitiBike for. 
    Together, the trip duration summary and box plot offer a concise view of how long bikes remain in use and how usage differs 
    by rider type — an important piece of understanding overall demand and how the system is used throughout the city.
    """)

    # --------------------------------
    # TWO-COLUMN LAYOUT
    # --------------------------------
    col1, col2 = st.columns([2, 1])

    # Left column — Box Plot
    with col1:
        st.image(
            "04_Analysis/Visualizations/tripduration_boxplot_static.png",
            use_column_width=True
        )

    # Right column — Summary (centered + tight)
    with col2:
        st.markdown(
            """
            <div style='text-align:center; margin-bottom:10px;'>
                <h2 style='margin-bottom:2px;'>Trip Duration Summary</h2>
                <p style='font-size:18px; margin-top:0px; color:#555;'>(1–65 Minutes)</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("""
        - **Median trip duration:** 10.0 minutes  
        - **Average trip duration:** 13.3 minutes  
        - **Shortest trip:** 1.0 minute  
        - **Longest trip:** 65.4 minutes  
        """)


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