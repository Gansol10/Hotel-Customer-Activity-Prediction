import streamlit as st
import eda
import prediction
import seaborn

Navigation = st.sidebar.selectbox('Pilih Halaman:', ('EDA','Predict Visitors Hotel Reservation'))
if Navigation == 'EDA':
    eda.run()
else:
    prediction.run()