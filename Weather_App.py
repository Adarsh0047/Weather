import streamlit as st
from PIL import Image
st.set_page_config("Weather App", layout="wide", page_icon="cloudy.png")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
st.title("Welcome to the Weather App")
st.balloons()
with st.expander("Know More"):
  st.write("This app was created by Adarsh using streamlit")
st.markdown("### Please use the sidebar for navigation")
st.markdown("""
[Github](https://github.com/Adarsh0047/Weather/tree/main)
""")
