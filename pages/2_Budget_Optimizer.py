import streamlit as st
from services.orchestrate_service import generate_trip

st.set_page_config(page_title="Budget Optimizer", page_icon="💰")

st.title("💰 AI Budget Optimizer")
st.write("Optimize your travel budget using IBM watsonx Orchestrate.")

source = st.text_input("Source")
destination = st.text_input("Destination")

budget = st.number_input(
    "Total Budget (₹)",
    min_value=1000,
    step=500
)

days = st.number_input(
    "Duration (Days)",
    min_value=1,
    value=3
)

travelers = st.number_input(
    "Number of Travelers",
    min_value=1,
    value=2
)

travel_type = st.selectbox(
    "Travel Type",
    ["Budget", "Standard", "Luxury"]
)

if st.button("Optimize Budget"):
        prompt = f"""
Optimize the travel budget for this trip.

Source: {source}
Destination: {destination}
Budget: ₹{budget}
Duration: {days} days
Travelers: {travelers}
Travel Type: {travel_type}
"""

        with st.spinner("Optimizing Budget..."):
            response = generate_trip(prompt)

        st.markdown(response)