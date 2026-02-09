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
    ["Overview", "Daily Rides vs Weather", "Trip Duration", "Top Stations", "Trip Hotspots", "Insights & Recommendations"]
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

NOTE: Use the **Navigate to** in the sidebar to move between sections.
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

    NOTE: Use the "Filter by Season" section in the sidebar to navigate various seasons.
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
                Top 20 Most Popular CitiBike Stations in NYC
            </h1>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------
    # IMAGE
    # --------------------------------
    img_left, img_center, img_right = st.columns([0.38, 1, 0.62])
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
        st.image("04_Analysis/Visualizations/top station.jpg")
        st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------
    # INSIGHTS
    # --------------------------------
    st.markdown("""
The top 20 CitiBike stations represent the busiest points in the network, reflecting where large numbers of people move through the city each day. These stations tend to be located in areas with dense foot traffic, strong transit connections, and easy‑to‑spot locations that riders naturally encounter as they move through the area. The pattern aligns with the broader spatial trends seen in the Geographic Trip Hotspots map, where Midtown, Lower Manhattan, and key waterfront areas emerge as consistent activity centers. Together, these high‑volume stations illustrate where CitiBike demand is most concentrated and where the system experiences the greatest day‑to‑day pressure to keep bikes available.
    """)

    # --------------------------------
    # Sort DATA for plotting
    # --------------------------------
    top20 = top_stations_df.sort_values("value", ascending=True)

    # --------------------------------
    # PLOT
    # --------------------------------
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
        title="Top 20 Stations",
        xaxis_title="Ride Count",
        yaxis_title="Station Name",
        template="plotly_white",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

################################################ CitiBike NYC Trip Hotspots (500 Busiest Routes) ################################################

## Trip Flow Map
# ---------------------------------------------------------
# Setup sidebar link
elif page == "Trip Hotspots":

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
                NYC CitiBike – Top 500 Trip Routes
            </h1>
            """,
            unsafe_allow_html=True
        )

    # Insights of the chart
    # ---------------------------------------------------------
    st.markdown("""

    The top 500 CitiBike trip flows reveal the strongest routes in the network, highlighting where riders most frequently travel between stations. These patterns cluster around Midtown, Lower Manhattan, and key waterfront areas, reflecting a mix of commuter routes, short neighborhood hops, and popular recreational pathways. These trip patterns also align with the station‑level trends shown on the “Top 20 Stations” page, reinforcing how rider activity concentrates around areas with heavy foot traffic, strong transit access, and well‑established bike‑friendly routes. A noticeable cluster of high‑volume routes appears along the southern edge of Central Park, where several nearby stations consistently rank among the busiest in the system.

    NOTE: You can use the left‑side editing panel to access the filter options; it opens by default and can be collapsed with the arrow button. The small panel in the top‑right corner of the map provides quick access to basic map controls.
     
         """)

    st.subheader("Top 500 Trips")

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
elif page == "Insights & Recommendations":

    # --------------------------------
    # TITLE
    # --------------------------------
    title_left, title_center, title_right = st.columns([0.38, 1, 0.62])
    with title_center:
        st.markdown(
            """
            <h1 style='text-align:center; font-size:46px; margin-top:0px; margin-bottom:10px;'>
                Insights & Recommendations
            </h1>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------
    # INSIGHTS
    # --------------------------------
    st.markdown("""
### Insights

The weather has a clear and predictable impact on CitiBike ridership. Colder temperatures consistently reduce daily ride counts, while warmer seasons support higher usage. November is a strong example: ridership remains high early in the month, but once temperatures drop, the number of rides falls sharply. This lower demand period continues through mid-April, when warmer weather brings ridership back up. These seasonal shifts highlight the importance of adjusting bike distribution throughout the year. Customer type also plays a role in how the system is used. Members tend to take more short trips compared to casual riders, suggesting that membership behavior is tied to quick, routine travel rather than longer recreational rides. Understanding these patterns can help tailor incentives and operational decisions to better support each rider group. The most popular stations and the top routes provide a clear picture of where demand is concentrated. High traffic areas, especially those with strong public transportation access, heavy foot traffic, and intuitive bike-friendly paths, consistently appear at the top of both lists. These insights help identify where additional stations, more docks, or increased bike availability would have the greatest impact.
""")

    # --------------------------------
    # RECOMMENDATIONS
    # --------------------------------
    st.markdown("""
### Recommendations

During the colder months, when overall ridership drops, bikes should be prioritized at the most consistently popular stations. This ensures that the riders who continue using the system during the off‑season still have reliable access. In contrast, during the peak spring and summer seasons, CitiBike should consider adding more stations or expanding existing ones in the high‑demand areas identified in the analysis. Given that members take more short trips, CitiBike could explore seasonal promotions tailored to this group. During peak months, small incentives, such as discounts for returning bikes to specific stations, could help reduce the need for frequent restocking. In the off‑season, stronger incentives or cost‑saving promotions could help boost ridership when demand naturally declines. A rewards or points system for members could also encourage more consistent usage throughout the year. Offering higher rewards during the down‑season would help balance demand and keep riders engaged. Finally, understanding the top stations and most frequently traveled routes provides a roadmap for operational planning. These insights can inform decisions about where to place new stations, where to expand dock capacity, and where to allocate additional bikes to meet demand. Strengthening the busiest corridors, particularly those surrounding transit hubs, waterfronts, and Central Park, would support the natural flow of rider behavior and enhance overall system reliability.
""")

    # --------------------------------
    # IMAGE
    # --------------------------------
    st.image("04_Analysis/Visualizations/recommendations.jpg", use_column_width=True)

