import streamlit as st
with open("style/style.css", "r") as f:
    css = f.read()




def initialize_page():
    st.markdown(
        f"""
        <style>
        {css}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        """
        <a class="sidebar-link" href="https://www.facebook.com/datasciencepjatk">Facebook</a><br>
        <a class="sidebar-link" href="https://dsc.pja.edu.pl/">Strona internetowa</a><br>
        <a class="sidebar-link" href="https://www.linkedin.com/company/datasciencepjatk/">LinkedIn</a><br>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.caption("2023 (data hardcodowana XD) Data Science Club PJATK")

