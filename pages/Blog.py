from render_project import render_project
from find_project import find_project
from initialize_page import initialize_page

initialize_page()
streamlit_project = find_project("Blog")
render_project(streamlit_project)