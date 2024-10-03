# utils/salvar_dados.py

import pandas as pd
import streamlit as st

def salvar_dataframe(df):
    """
    Função para salvar um DataFrame como CSV e permitir o download pelo Streamlit.
    """
    csv = df.to_csv(index=False)
    st.download_button(
        label="Baixar Dados",
        data=csv,
        file_name="similaridade_linguistica.csv",
        mime="text/csv"
    )
