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
    
    colunas = ["X", "Y", "ID", "NM", "RESPON", "DINI", "DFIM", "MED_ANUAL", "MIN_ANUAL", "MAX_ANUAL", "N_JUL", "MED_JUL", "MIN_JUL", "MAX_JUL"]
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
    {"Coluna": "X", "Descrição": "Longitude", "Tipo": "Quantitativa contínua"},
    {"Coluna": "Y", "Descrição": "Latitude", "Tipo": "Quantitativa contínua"},
    {"Coluna": "ID", "Descrição": "Identificador da estação", "Tipo": "Qualitativa nominal"},
    {"Coluna": "NM", "Descrição": "Nome da estação", "Tipo": "Qualitativa nominal"},
    {"Coluna": "RESPON", "Descrição": "Responsável pela estação", "Tipo": "Qualitativa nominal"},
    {"Coluna": "DINI", "Descrição": "Data de início da coleta", "Tipo": "Qualitativa ordinal"},
    {"Coluna": "DFIM", "Descrição": "Data de fim da coleta", "Tipo": "Qualitativa ordinal"},
    {"Coluna": "MED_ANUAL", "Descrição": "Média anual de precipitação", "Tipo": "Quantitativa contínua"},
    {"Coluna": "MIN_ANUAL", "Descrição": "Mínima anual", "Tipo": "Quantitativa contínua"},
    {"Coluna": "MAX_ANUAL", "Descrição": "Máxima anual", "Tipo": "Quantitativa contínua"},
    {"Coluna": "N_JUL", "Descrição": "Quantidade de medições em julho", "Tipo": "Quantitativa discreta"},
    {"Coluna": "MED_JUL", "Descrição": "Média de precipitação em julho", "Tipo": "Quantitativa contínua"},
    {"Coluna": "MIN_JUL", "Descrição": "Mínimo em julho", "Tipo": "Quantitativa contínua"},
    {"Coluna": "MAX_JUL", "Descrição": "Máximo em julho", "Tipo": "Quantitativa contínua"},
    ]

    df_variaveis = pd.DataFrame(dados_variaveis)

    st.dataframe(df_variaveis, use_container_width=True)
