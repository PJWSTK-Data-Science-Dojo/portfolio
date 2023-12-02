#Streamlit app main file

import streamlit as st

st.set_page_config(
    page_title="Data Science Club PJATK",
    page_icon="🧊",
)

#Load css file
with open("style/style.css", "r") as f:
    css = f.read()
    
st.markdown(
    f"""
    <style>
    {css}
    </style>
    """,
    unsafe_allow_html=True
)

st.write("# HelloWorld('print')")

st.sidebar.markdown(
    """
    <a class="sidebar-link" href="https://www.facebook.com/datasciencepjatk">Facebook</a><br>
    <a class="sidebar-link" href="https://dsc.pja.edu.pl/">Strona internetowa</a><br>
    <a class="sidebar-link" href="https://www.linkedin.com/company/datasciencepjatk/">LinkedIn</a><br>
    """,
    unsafe_allow_html=True
)
st.sidebar.caption("2023 (data hardcodowana XD) Data Science Club PJATK")

st.markdown(
    """
    <i>Lorem Ipsum</i> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
    standard dummy text ever since the 1500s, when an unknown printer took a <b>galley</b> of type and scrambled it to make a type specimen book.
    It has survived not only five centuries, but also the leap into electronic <u>typesetting</u>, remaining essentially unchanged.
    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
    and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    
    <br><br>
    
    <div id = "red-text">
    W markdownach możemy dodawać div'y. CSS edytujemy w pliku style/style.css
    </div>
    
    """, unsafe_allow_html=True
)

