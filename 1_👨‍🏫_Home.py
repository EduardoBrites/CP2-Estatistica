import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo
import time

if "data" not in st.session_state:
    df = pd.read_csv("bebedouro_ana_proximidades_TSA.csv")
    st.session_state["data"] = df

# Configuração da página
st.set_page_config(page_title="CP2 Análise de dados pluviométricos", layout="wide")

col1, col2= st.columns([1, 3])

with col1:
    subcol1, subcol2, subcol3 = st.columns([2, 3, 2])
    with subcol2:
        st.write("")
        st.write("")

        st.image("img/rain_drop.svg", use_container_width=True)
with col2:
    st.title("Checkpoint 2 | Estatística")

st.title("")

col1, col2, col3 = st.columns([1, 10, 1])

with col2:
    st.markdown(
        """
        <style>
            .justificado {
                text-align: justify;
            }
        </style>

        <h2>Problema</h2>
    
        <br>
        <p class="justificado"></p>
        """,
        unsafe_allow_html=True
        )