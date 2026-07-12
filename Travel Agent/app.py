import streamlit as st

st.set_page_config(
    page_title="Travel Intelligence AI",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🌍 Travel Intelligence AI")
st.subheader("Powered by IBM watsonx Orchestrate")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧳 Travel Planner")
    st.write("Generate personalized travel itineraries using IBM watsonx Orchestrate.")

    if st.button("Open Travel Planner", use_container_width=True):
        st.switch_page("pages/1_Trip_Planner.py")

with col2:
    st.subheader("💰 Budget Optimizer")
    st.write("Optimize your travel budget using AI.")

    if st.button("Open Budget Optimizer", use_container_width=True):
        st.switch_page("pages/2_Budget_Optimizer.py")