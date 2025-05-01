import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Base de Dados",
    page_icon="🎲",
    layout="wide"
)

df = st.session_state["data"]

col1, col2= st.columns([1, 3])

with col1:
    subcol1, subcol2, subcol3 = st.columns([2, 1, 2])
    with subcol2:
        st.write("")
        st.write("")

        st.image("img/database.svg", use_container_width=True)
with col2:
    st.write("")
    st.title("Base de Dados")

st.title("")

col1, col2, col3 = st.columns([1, 10, 1])

with col2:
    st.markdown("""
        <style>
            .justificado {
                text-align: justify;
            }
        </style>

        <h2>Descrição</h2>

        <p class="justificado">A base de dados descrita nesse arquivo foi disponibilizada pela Agência Nacional de Águas e Saneamento Básico (ANA), contendo 1.32 MB de dados, dispostos em 324 colunas e 230 linhas, os quais podem ser visualizados a baixo:</p>
        """,
        unsafe_allow_html=True
        )
    st.write(df)
    
    st.write("")
    st.markdown("""
        <style>
            .justificado {
                text-align: justify;
            }
        </style>

        <h2>Dados Escolhidos</h2>

        <p class="justificado">Para a análise descrita nesse projeto alguns dados foram priorizados, nesse caso, os dados referentes as estações de coleta de Ribeirão Preto nos meses de julho</p>
        """,
        unsafe_allow_html=True
        )
    filtro = df["NM"].str.contains("RIBEIRÃO PRETO", case=False, na=False)
    df_filtrado = df[filtro]
    
    colunas = ["NM", "MIN_JAN", "MED_JAN", "MAX_JAN",
        "MIN_FEV", "MED_FEV", "MAX_FEV",
        "MIN_MAR", "MED_MAR", "MAX_MAR",
        "MIN_ABR", "MED_ABR", "MAX_ABR",
        "MIN_MAI", "MED_MAI", "MAX_MAI",
        "MIN_JUN", "MED_JUN", "MAX_JUN",
        "MIN_JUL", "MED_JUL", "MAX_JUL",
        "MIN_AGO", "MED_AGO", "MAX_AGO",
        "MIN_SET", "MED_SET", "MAX_SET",
        "MIN_OUT", "MED_OUT", "MAX_OUT",
        "MIN_NOV", "MED_NOV", "MAX_NOV",
        "MIN_DEZ", "MED_DEZ", "MAX_DEZ"]
    df_rp = df_filtrado[colunas]
    st.write(df_rp)

    st.write("")
    st.markdown("""
        <style>
            .justificado {
                text-align: justify;
            }
        </style>

        <h2>Dicionário de dados</h2>

        <p class="justificado">Abaixo estão as variáveis do conjunto de dados, suas descrições e seus tipos estatísticos:</p>
        """,
        unsafe_allow_html=True
        )
    dados_variaveis = [
        {"Coluna": "NM", "Descrição": "Nome da estação", "Tipo": "Qualitativa nominal"},
        {"Coluna": "MIN_JAN", "Descrição": "Mínimo em janeiro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MED_JAN", "Descrição": "Média de precipitação em janeiro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MAX_JAN", "Descrição": "Máximo em janeiro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MIN_FEV", "Descrição": "Mínimo em fevereiro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MED_FEV", "Descrição": "Média de precipitação em fevereiro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MAX_FEV", "Descrição": "Máximo em fevereiro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MIN_MAR", "Descrição": "Mínimo em março", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MED_MAR", "Descrição": "Média de precipitação em março", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MAX_MAR", "Descrição": "Máximo em março", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MIN_ABR", "Descrição": "Mínimo em abril", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MED_ABR", "Descrição": "Média de precipitação em abril", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MAX_ABR", "Descrição": "Máximo em abril", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MIN_MAI", "Descrição": "Mínimo em maio", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MED_MAI", "Descrição": "Média de precipitação em maio", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MAX_MAI", "Descrição": "Máximo em maio", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MIN_JUN", "Descrição": "Mínimo em junho", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MED_JUN", "Descrição": "Média de precipitação em junho", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MAX_JUN", "Descrição": "Máximo em junho", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MIN_JUL", "Descrição": "Mínimo em julho", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MED_JUL", "Descrição": "Média de precipitação em julho", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MAX_JUL", "Descrição": "Máximo em julho", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MIN_AGO", "Descrição": "Mínimo em agosto", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MED_AGO", "Descrição": "Média de precipitação em agosto", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MAX_AGO", "Descrição": "Máximo em agosto", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MIN_SET", "Descrição": "Mínimo em setembro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MED_SET", "Descrição": "Média de precipitação em setembro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MAX_SET", "Descrição": "Máximo em setembro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MIN_OUT", "Descrição": "Mínimo em outubro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MED_OUT", "Descrição": "Média de precipitação em outubro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MAX_OUT", "Descrição": "Máximo em outubro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MIN_NOV", "Descrição": "Mínimo em novembro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MED_NOV", "Descrição": "Média de precipitação em novembro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MAX_NOV", "Descrição": "Máximo em novembro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MIN_DEZ", "Descrição": "Mínimo em dezembro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MED_DEZ", "Descrição": "Média de precipitação em dezembro", "Tipo": "Quantitativa contínua"},
        {"Coluna": "MAX_DEZ", "Descrição": "Máximo em dezembro", "Tipo": "Quantitativa contínua"}
    ]

    df_variaveis = pd.DataFrame(dados_variaveis)

    st.dataframe(df_variaveis, use_container_width=True)
