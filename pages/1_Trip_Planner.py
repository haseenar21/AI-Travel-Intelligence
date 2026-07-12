import streamlit as st
# from services.orchestrate_service import test_connection
from services.orchestrate_service import generate_trip

st.title("✈️ Travel Planner")

source = st.text_input("Source City")

destination = st.text_input("Destination")

days = st.slider(
    "Trip Duration (Days)",
    1,
    15,
    5
)

budget = st.number_input(
    "Budget (₹)",
    min_value=1000,
    value=20000,
    step=1000
)

travelers = st.number_input(
    "Number of Travelers",
    min_value=1,
    value=2
)

travel_type = st.selectbox(
    "Travel Type",
    [
        "Solo",
        "Family",
        "Couple",
        "Business",
        "Friends"
    ]
)

interests = st.multiselect(
    "Interests",
    [
        "Nature",
        "Food",
        "Friends",
        "History",
        "Shopping",
        "Wildlife",
        "Photography"
    ]
)

if st.button("Generate Travel Plan"):

    prompt = f"""
    Source: {source}

    Destination: {destination}

    Duration: {days} days

    Budget: ₹{budget}

    Travelers: {travelers}

    Travel Type: {travel_type}

    Interests: {', '.join(interests)}

    Generate a complete travel itinerary.
    """

    response = generate_trip(prompt)

    st.write(response)