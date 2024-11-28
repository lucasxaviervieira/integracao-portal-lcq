import streamlit as st
import pandas as pd

from utils.clean_xl.steps import *

st.title("Adicione a amostra mensal")

uploaded_file = st.file_uploader("Envie um arquivo Excel", type=["xlsx", "xls"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, header=None)
        new_df = new_header(df, uploaded_file)
        new_df = concatenate_columns(new_df)
        st.write(new_df)

        st.write(new_df.columns)
    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")
else:
    st.info("Envie um arquivo para continuar.")
