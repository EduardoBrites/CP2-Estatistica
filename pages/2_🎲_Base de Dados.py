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

st.title("Base de Dados", anchor=False)

st.write("")

estacao = df.groupby("ID")["NM"].sum()
st.write(df)
st.write(estacao)

st.write("Estação escolhida: Ribeirão Preto")