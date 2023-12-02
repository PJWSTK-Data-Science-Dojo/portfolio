from render_project import render_project
from find_project import find_project
from initialize_page import initialize_page
from PIL import Image


import streamlit as st

st.set_page_config(page_title="Streamlit - O nas", page_icon="🧊")
initialize_page()
image = Image.open("images/dsc_logo.png")
st.image(image, caption="DSC PJATK")

streamlit_project = find_project("Streamlit")
render_project(streamlit_project)



