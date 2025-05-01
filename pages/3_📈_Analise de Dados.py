import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import plotly.graph_objects as go
import seaborn as sns

st.set_page_config(
    page_title="Dados",
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

        st.image("img/analisis.svg", use_container_width=True)
with col2:
    st.write("")
    st.title("Análise de dados")

st.title("")

col1, col2, col3 = st.columns([1, 10, 1])

with col2:
    
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
    st.markdown(
        """
        <style>
            .justificado {
                text-align: justify;
            }
        </style>

        <h2>Intervalo de Confiança</h2>
        """,
        unsafe_allow_html=True
        )
    

    meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 
         'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']

    # Inicializar listas para os resultados
    min_mensal = []
    med_mensal = []
    max_mensal = []
    erro_padrao_mensal = []
    
    for mes in meses:
        col_min = f"MIN_{mes}"
        col_med = f"MED_{mes}"
        col_max = f"MAX_{mes}"
        
        # Calcular a menor mínima, média das médias e maior máxima
        menor_min = df_rp[col_min].min()
        media_med = df_rp[col_med].mean()
        maior_max = df_rp[col_max].max()
        
        # Calcular o erro padrão para a média (considerando n como o número de estações)
        erro_padrao = df_rp[col_med].std() / np.sqrt(len(df_rp))
        
        # Adicionar aos resultados
        min_mensal.append(menor_min)
        med_mensal.append(media_med)
        max_mensal.append(maior_max)
        erro_padrao_mensal.append(erro_padrao)
    
    # Criar DataFrame consolidado
    df_resultado = pd.DataFrame({
        'Mês': meses,
        'Menor Índice Pluviométrico': min_mensal,
        'Média dos Índices': med_mensal,
        'Maior Índice Pluviométrico': max_mensal,
        'Erro Padrão': erro_padrao_mensal
    })
    
    # Streamlit: título
    st.title('Resumo Mensal dos Índices Pluviométricos com Intervalo de Confiança')
    
    # Streamlit: exibir tabela de resultados
    st.write(df_resultado)
    
    # Plotando o gráfico de barras com erro padrão
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Barra de média dos índices
    ax.bar(df_resultado['Mês'], df_resultado['Média dos Índices'], yerr=df_resultado['Erro Padrão'], capsize=5, label='Média dos Índices', color='skyblue')
    
    # Adicionando as linhas de intervalo de confiança
    ax.errorbar(df_resultado['Mês'], df_resultado['Média dos Índices'], yerr=df_resultado['Erro Padrão'], fmt='o', color='black', label='Intervalo de Confiança (Erro Padrão)')
    
    ax.set_title('Média dos Índices Pluviométricos com Intervalo de Confiança (Erro Padrão)')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Índice Pluviométrico (mm)')
    ax.legend()
    ax.grid(True)
    
    # Exibir o gráfico no Streamlit
    st.pyplot(fig)
    
    
    
    
    