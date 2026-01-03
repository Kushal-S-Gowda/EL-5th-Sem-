import sys
import os
import streamlit as st
import plotly.graph_objects as go

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from run_optimizer import run_pipeline
from road_grid_layout import generate_rectangular_masterplan
from plot_styles import ROAD_COLOR, RESIDENTIAL_COLOR, COMMERCIAL_COLOR, PARK_COLOR, BORDER

st.set_page_config("SmartCitySim – AI Driven Masterplan", layout="wide")
st.title("🏙️ SmartCitySim – AI Driven Urban Masterplan")

if st.sidebar.button("🚀 Generate AI Optimized Layout"):

    contract = run_pipeline()
    layout = generate_rectangular_masterplan(contract)

    fig = go.Figure()

    for road in layout["roads"]:
        x, y = road.exterior.xy
        fig.add_trace(go.Scatter(
            x=list(x), y=list(y),
            fill="toself",
            fillcolor=ROAD_COLOR,
            line=dict(color=BORDER),
            hoverinfo="skip"
        ))

    for park in layout["parks"]:
        x, y = park.exterior.xy
        fig.add_trace(go.Scatter(
            x=list(x), y=list(y),
            fill="toself",
            fillcolor=PARK_COLOR,
            line=dict(color=BORDER),
            hoverinfo="text",
            text="Park"
        ))

    for c in layout["commercial_plots"]:
        x, y = c.exterior.xy
        fig.add_trace(go.Scatter(
            x=list(x), y=list(y),
            fill="toself",
            fillcolor=COMMERCIAL_COLOR,
            line=dict(color=BORDER),
            text="Commercial"
        ))

    for p in layout["residential_plots"]:
        poly = p["geometry"]
        x, y = poly.exterior.xy
        cx, cy = poly.centroid.xy

        fig.add_trace(go.Scatter(
            x=list(x), y=list(y),
            fill="toself",
            fillcolor=RESIDENTIAL_COLOR,
            line=dict(color=BORDER),
            hoverinfo="text",
            text=f"""
Plot {p['id']}
{p['width_m']} × {p['depth_m']} m
Area: {p['area_sqm']} sqm
Max Height: {p['height_allowed']} m
"""
        ))

        fig.add_trace(go.Scatter(
            x=[cx[0]], y=[cy[0]],
            mode="text",
            text=str(p["id"]),
            textfont=dict(size=10)
        ))

    fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=850,
        plot_bgcolor="#f4f4f4",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)
