import streamlit as st
from PIL import Image


st.write("cheatsheet (https://docs.streamlit.io/library/cheatsheet)")


image = Image.open("images/dsc_logo.png")
st.image(image, caption="DSC PJATK")
