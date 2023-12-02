from Project import Project
import streamlit as st

def render_project(proj: Project):
    st.title(proj.project_name, anchor="Name")
    st.markdown(proj.project_description)

    if len(proj.project_goal) > 0:
        st.header("Cel projekta")
        st.markdown(proj.project_goal)


    if len(proj.project_members) > 0:
        st.header("Kto to robi?")
        for per in proj.project_members:
            st.markdown("- " + per)

    if len(proj.start_time) > 0:
        st.header("Ile czasu trwa już ten projekt?")
        st.markdown("**Rozpoczęcie:** "+proj.start_time)
        st.markdown("**Czasu użyto:** " + proj.spent_time)

    if len(proj.tests_and_their_results) > 0:
        st.header("Jakie są wyniki badań czyli testów tego projekta?")
        for test in proj.tests_and_their_results:
            st.markdown("#### " + test["name"])
            st.markdown(test["description_md"])
            st.markdown("Rezultat: " + test["result"])
