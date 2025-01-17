import streamlit as st
import pandas as pd

from core.clean_xl.index import clean_excel
from core.insert_df.index import insert_dataframe


def main_app():
    st.title("Adicione a amostra mensal")

    uploaded_file = st.file_uploader("Envie um arquivo Excel", type=["xlsx", "xls"])

    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file, header=None)

            new_df = clean_excel(df, uploaded_file)

            len_df = len(new_df)
            st.write(f"Quantidade de amostras liberadas: {len_df}")
            st.write(new_df)

            if st.button(f"Adicionar as {len_df} amostras liberadas"):
                message = insert_dataframe(new_df)
                st.write(message)

        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {e}")
    else:
        st.info("Envie um arquivo para continuar.")
