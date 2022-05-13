import streamlit as st
from PIL import Image
import tensorflow as tf
import pandas as pd
import pickle

def app():
    model = tf.keras.models.load_model("model.h5")
    with open("preprocessor.pkl", "rb") as f:
        preprocessor = pickle.load(f)

    # PT TELCO
    st.markdown(
        "<h1 style='text-align: center'> <strong>TELCO CHURN PREDICTION APPLICATION<strong> </h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<h3 style="text-align: center"><strong>Anita Antono</strong><br><br></h3>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<h3 style="text-align: center"><strong>Phase 2 - Milestone 1 Project</strong><br><br></h3>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<h4 style="text-align: center"><strong>Artificial Neural Network</strong>🧠<br><br></h4>',
        unsafe_allow_html=True,
    )

    st.markdown("<img src='https://miro.medium.com/max/1003/1*kU_mPtwcjfEUSkSflUikxw.jpeg' width='100%'/>", unsafe_allow_html=True)

    # customer information
    st.markdown(
        '<hr><h3 style="text-align: center">Customer Information</h3>',
        unsafe_allow_html=True,
    )
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gender = st.selectbox("Customer 🕺🏻💃🏻 Gender", ["Male", "Female"])
    with col2:
        seniorcitizen = st.selectbox(
            "Is the customer a 👨🏻‍🦳 senior citizen 🧑🏻‍🦳 ? ", ["No", "Yes"]
        )
    with col3:
        partner = st.selectbox("Do the customer has partner 👩🏻‍❤️‍👨🏻 ?", ["No", "Yes"])
    with col4:
        dependent = st.selectbox(
            "Does the customer has dependent ? 👨‍👩‍👧‍👦", ["No", "Yes"]
        )
    tenure = st.number_input(
        "📆 How long customer being 'a customer' ?", min_value=1
    )

    # CUSTOMER PHONE SERVICE SECTION
    st.markdown(
        '<hr><h3 style="text-align: center">Company Services</h3>', unsafe_allow_html=True
    )
    col5, col6 = st.columns(2)
    with col5:
        phoneservice = st.selectbox("☎️☎️☎️ Phone Service", ["No", "Yes"])
    if phoneservice == "Yes":
        with col6:
            multipleLines = st.selectbox("☎️ 🖥️ 📺 Multiple Lines", ["No", "Yes"])
    else:
        multipleLines = "No phone service"

    # CUSTOMER INTERNET SERVICE SECTION
    st.markdown(
        '<hr><h3 style="text-align: center">Internet Services</h3>',
        unsafe_allow_html=True,
    )
    internetservice = st.selectbox(
        "🖥️📡 Internet Service", ["Fiber optic", "DSL", "No"]
    )

    # CUSTOMER ADDITIONAL SERVICE SECTION
    if internetservice != "No":
        st.markdown(
            '<hr><h4 style="text-align: center">Protection Service</h4>',
            unsafe_allow_html=True,
        )
        col7, col8, col9, col10 = st.columns(4)
        with col7:
            onlineSecurity = st.selectbox("👮🏻👮🏼‍♀️ Online Security", ["No", "Yes"])
        with col8:
            onlineBackup = st.selectbox("🧑🏻‍💻👩🏻‍💻 Online Backup", ["No", "Yes"])
        with col9:
            deviceProtection = st.selectbox("🦾📲 Device Protection", ["No", "Yes"])
        with col10:
            techSupport = st.selectbox("💻🤳🏻 Tech Support", ["No", "Yes"])
        st.markdown(
            '<hr><h4 style="text-align: center">Streaming Service</h4>',
            unsafe_allow_html=True,
        )
        col11, col12 = st.columns(2)
        with col11:
            streamingTV = st.selectbox("Streaming TV 📡📺", ["No", "Yes"])
        with col12:
            streamingMovies = st.selectbox("Streaming Movies 📽️🍿", ["No", "Yes"])
    else:
        onlineSecurity = (
            onlineBackup
        ) = (
            deviceProtection
        ) = techSupport = streamingTV = streamingMovies = "❌❌No internet service❌❌"

    # billing
    st.markdown(
        '<hr><h3 style="text-align: center">Billing Information</h3>',
        unsafe_allow_html=True,
    )
    col13, col14, col15 = st.columns(3)
    with col13:
        contract = st.selectbox(
            "contract", ["Month-to-month", "One year", "Two year"]
        )
    with col14:
        paperlessbilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    with col15:
        paymentmethod = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer(automatic)",
                "Credit card(automatic)",
            ],
        )
    col16, col17 = st.columns(2)
    with col16:
        monthlycharges = st.number_input("monthly charges", min_value=20)
    with col17:
        totalcharges = st.number_input("total charges", min_value=0)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Create dictionary with all customer information
    data = {
        "gender": gender,
        "seniorcitizen": seniorcitizen,
        "partner": partner,
        "dependents": dependent,
        "tenure": tenure,
        "phoneservice": phoneservice,
        "multiplelines": multipleLines,
        "internetservice": internetservice,
        "onlinesecurity": onlineSecurity,
        "onlinebackup": onlineBackup,
        "deviceprotection": deviceProtection,
        "techsupport": techSupport,
        "streamingtv": streamingTV,
        "streamingmovies": streamingMovies,
        "contract": contract,
        "paperlessbilling": paperlessbilling,
        "paymentmethod": paymentmethod,
        "monthlycharges": monthlycharges,
        "totalcharges": totalcharges,
    }

    col18, col19, col20 = st.columns([1.7, 1, 1])
    with col19:
        predict = st.button("Prediction")

    # PREDICTION SECTION
    if predict:
        data_df = pd.DataFrame(data, index=[0])  # convert dict to dataframe

        data_df = preprocessor.transform(data_df)  # preprocess data

        prediction = model.predict(data_df).round()  # predict

        if prediction == 1:
            # if customer is likely to churn
            st.markdown(
                '<h2 style="text-align: center">😞 Customer<span style="color: red"> SAY GOOD BYE! </span> 😰👋🏻 </h2>',
                unsafe_allow_html=True,
            )
        else:
            # if customer is likely to stay
            st.markdown(
                '<h2 style="text-align: center">🥳 YEAAAYY!!! Customer will <span style="color: blue"> stay </span> with us! 🥳🥳</h2>',
                unsafe_allow_html=True,
            )

    # note:
    # 1 is churn
    # 0 is stay