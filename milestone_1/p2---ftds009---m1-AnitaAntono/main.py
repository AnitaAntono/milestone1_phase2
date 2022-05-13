import streamlit as st


def app():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(
            "<h1 style='text-align: center;'>Welcome!👩🏻‍🍳 </h1>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<h3 style='text-align: center;'><strong>This my app to predict churn with <strong>NEURAL NETWORK 🧠</strong></h3>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='text-align: center;'>kindly check the dataset here 👉🏻<a href='https://www.kaggle.com/blastchar/telco-customer-churn'>Kaggle</a>.</p>",
            unsafe_allow_html=True,
        )

        with st.expander("Tap Here 👇🏽"):
            st.markdown(
                "<img src='https://media0.giphy.com/media/KheNHe2jPcwkmThceS/giphy.gif?cid=ecf05e479ip89dhysugtk3l4w16jox0el5eqm2ytgts0dscc&rid=giphy.gif&ct=g' width='100%'/>",
                unsafe_allow_html=True,
            )
        st.markdown(
            "<p style='text-align: center;'>Created by <span style='color: blue'> 🙋🏻‍♀️ </span> by <b>Anita Antono ♥️</b></p>",
            unsafe_allow_html=True,
        )