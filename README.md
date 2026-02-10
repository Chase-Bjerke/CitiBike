# CitiBike Strategy Dashboard

A data-driven exploration of New York City’s CitiBike system, designed to help the business strategy team understand usage patterns, identify operational bottlenecks, and support smarter bike distribution across the city.

This dashboard transforms raw trip data into clear, actionable insights through interactive visualizations, spatial analysis, and narrative recommendations.

---

## Project Overview

New York City’s CitiBike network experiences uneven demand across seasons, neighborhoods, and rider types. These fluctuations can lead to availability issues—empty docks in high‑demand areas and overcrowded stations elsewhere.

As the lead analyst, the goal of this project is to:

- Diagnose where and why distribution issues occur  
- Understand how weather, geography, and rider behavior shape demand  
- Provide clear, actionable recommendations to improve system reliability  
- Present insights in a clean, intuitive dashboard for strategic decision‑making  

This dashboard is built using Python, Streamlit, Pandas, Plotly, and Kepler.gl.

---

## Dashboard Structure

The dashboard is organized into six pages, each focusing on a key dimension of CitiBike system performance.

### **1. Overview**
Introduces the project’s purpose, analytical approach, and the core questions guiding the investigation.

### **2. Daily Rides vs Weather**
A dual‑axis chart showing how temperature influences daily ridership.  
Key patterns include:

- Strong seasonal correlation  
- Sharp declines in colder months  
- Peak ridership in late summer and early fall  

### **3. Trip Duration**
A comparison of trip lengths between Members and Casual Riders.  
Insights reveal:

- Members take shorter, more consistent trips  
- Casual riders take longer, more variable trips  
- Trip duration reflects purpose: commuting vs recreation  

### **4. Top Stations**
A horizontal bar chart of the 20 busiest stations in NYC.  
These stations cluster around:

- Midtown  
- Lower Manhattan  
- Transit hubs  
- Waterfronts  

### **5. Trip Hotspots**
A Kepler.gl map visualizing the top 500 most-traveled routes.  
This spatial analysis highlights:

- Strong commuter corridors  
- Recreational loops near Central Park  
- Dense activity around transit-heavy neighborhoods  

### **6. Insights & Recommendations**
A narrative summary of the most important findings, followed by strategic recommendations for:

- Seasonal bike allocation  
- Membership incentives  
- Dock expansion  
- Corridor strengthening  

---

## Deployment

This dashboard is deployed using Streamlit Cloud and updates automatically when changes are pushed to the repository.

Live App:  
https://citibike-4app9pxamtuuyrqmhstmttp.streamlit.app/

---

## Key Insights

- Weather drives demand: ridership rises with temperature and falls sharply in winter.  
- Members behave differently: shorter, more routine trips compared to casual riders.  
- Demand is geographically concentrated: Midtown, Lower Manhattan, and Central Park dominate activity.  
- Top routes reveal commuter corridors that require consistent bike availability.  

---

## Recommendations

- Prioritize bike availability at high‑demand stations during winter months.  
- Expand docks or add new stations in consistently overloaded areas.  
- Offer targeted incentives for members to balance demand.  
- Strengthen key corridors around transit hubs and recreational zones.  

---

## Tools & Technologies

- Python — Data processing and analysis  
- Pandas — Data cleaning and transformation  
- Plotly — Interactive charts and visualizations  
- Streamlit — Dashboard framework and deployment  
- Kepler.gl — Geospatial trip visualization  
- NumPy — Numerical operations  

---

## Project Structure

- 01_Data/  
  - Raw_Data/

- 02_Data/  
  - Prepared_Data/  
    - daily_sub_df.csv  
    - top_stations_df.csv  
    - kepler.gl.html  

- 03_Notebooks/  
  - 01_data_cleaning.ipynb  
  - 02_feature_engineering.ipynb  
  - 03_visual_exploration.ipynb  

- 04_Analysis/  
  - Visualizations/  
    - green_light_bike.jpg  
    - tripduration_boxplot_static.png  
    - top station.jpg  
    - recommendations.jpg  

- CitiBike_dashboard.py  
- requirements.txt  
- README.md

Disclaimer: This dashboard and analysis are for educational and demonstration purposes only and are not affiliated with or endorsed by CitiBike or Lyft.
