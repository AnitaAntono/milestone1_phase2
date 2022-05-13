import streamlit as st
import predict
import main

st.set_page_config(
    page_title="Churn Prediction",
    page_icon="🍯",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": "https://www.linkedin.com/in/anita-antono-0156656b/",
        "About": "Churn Prediction Application - by Anita Antono",
    },
)

PAGES = {"Main": main, "Prediction": predict}


st.sidebar.title("Menu")
page = st.sidebar.selectbox("Choose a page", list(PAGES.keys()))

page = PAGES[page]
page.app()