import streamlit as st
from PIL import Image
st.set_page_config("Weather Predictor",layout="wide",page_icon="cloudy.png")
st.title("Welcome to the Weather App")
st.balloons()
with st.expander("Know More"):
  st.write("This app was created by Adarsh S using streamlit")
st.markdown("### Please use the sidebar for navigation")
st.markdown("""
[Github](https://github.com/Adarsh0047/Weather/tree/main)
""")
