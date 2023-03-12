import streamlit as st
st.set_page_config(page_icon="about.png",layout="wide")
st.header("This app is used to predict the weather from images")
with st.expander("Know More"):
    st.write("The images can be uploaded from a local device or as a url from the web ")
