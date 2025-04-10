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
    subcol1, subcol2, subcol3 = st.columns([2, 1, 2])
    with subcol2:
        st.write("")
        st.write("")

        st.image("img/rain_drop.svg", use_container_width=True)
with col2:
    st.write("")
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

        <h2>Introdução</h2>

        <p class="justificado">Olá! Esse é um projeto que visa análisar os dados coletados pela Agência Nacional de Águas e Saneamento Básico (ANA). E a partir dessas análises responder alguns questionamentos sobre os dados pluviométricos anualmente coletados em específico pela estação de Ribeirão Preto</p>
        """,
        unsafe_allow_html=True
        )
    
    st.title("")
    st.markdown(
        """
        <style>
            .justificado {
                text-align: justify;
            }
        </style>

        <h2>Nossa equipe</h2>
        """,
        unsafe_allow_html=True
        )
    
    subcol1, subcol2, subcol3, subcol4, subcol5, subcol6, subcol7, subcol8, subcol9 = st.columns([1, 2, 1, 1, 2, 1, 1 ,2, 1])
    
    with subcol2:
        st.image("img/Eduardo.jpg", use_container_width=True)
        st.write("Eduardo Brites")
        
    with subcol5:
        st.image("img/Gabriel.jpg", use_container_width=True)
        st.write("Gabriel Leão")
        
    with subcol8:
        st.image("img/Karolina.jpg", use_container_width=True)
        st.write("Karolina Soares")
    
    