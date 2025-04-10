import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import plotly.graph_objects as go

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
    
    colunas = ["X", "Y", "ID", "NM", "RESPON", "DINI", "DFIM", "MED_ANUAL", "MIN_ANUAL", "MAX_ANUAL", "N_JUL", "MED_JUL", "MIN_JUL", "MAX_JUL"]
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
    
    filtro = df["NM"].str.contains("RIBEIRÃO PRETO", case=False, na=False)
    df_filtrado = df[filtro]
    
    colunas = ["X", "Y", "ID", "NM", "RESPON", "DINI", "DFIM", "MED_ANUAL", "MIN_ANUAL", "MAX_ANUAL", "N_JUL", "MED_JUL", "MIN_JUL", "MAX_JUL"]
    df_rp = df_filtrado[colunas]

    def intervalo_confianca(data, confidence=0.95):
        data = data.dropna()  # remove valores ausentes
        n = len(data)
        mean = np.mean(data)
        std_err = stats.sem(data)
        h = std_err * stats.t.ppf((1 + confidence) / 2, n - 1)
        return mean, mean - h, mean + h

    variaveis_analise = ['MED_JUL']
    resultados = []

    for var in variaveis_analise:
        media, ic_min, ic_max = intervalo_confianca(df_rp[var])
        resultados.append({
            "Variável": var,
            "Média": round(media, 2),
            "IC 95% Inferior": round(ic_min, 2),
            "IC 95% Superior": round(ic_max, 2)
        })

    df_ic = pd.DataFrame(resultados)
    st.dataframe(df_ic, use_container_width=True)
    
    #st.markdown("""<h2>Distribuições com Intervalos de Confiança</h2>""", unsafe_allow_html=True)

    #for var in variaveis_analise:
    #    dados = df_rp[var].dropna()
    #    media, ic_min, ic_max = intervalo_confianca(dados)

    #    fig, ax = plt.subplots(figsize=(10, 4))
    #    sns.histplot(dados, kde=True, bins=20, ax=ax, color="skyblue")
    #    ax.axvline(media, color='blue', linestyle='--', label=f'Média ({media:.2f})')
    #    ax.axvline(ic_min, color='red', linestyle=':', label=f'IC Inferior ({ic_min:.2f})')
    #    ax.axvline(ic_max, color='green', linestyle=':', label=f'IC Superior ({ic_max:.2f})')
    #    ax.set_title(f'Distribuição da variável {var}')
    #    ax.legend()
    #    st.pyplot(fig)

    subcol1, subcol2, subcol3 = st.columns([1, 4, 1])
    with subcol2:
        media_med_jul, ic_min_med_jul, ic_max_med_jul = intervalo_confianca(df_rp['MED_JUL'])

        fig, ax = plt.subplots()

        ax.scatter(df_rp["NM"], df_rp['MED_JUL'], label='Medições de Julho', s=20)
        plt.xticks(rotation=45, ha='right')

        ax.axhline(media_med_jul, color='red', linestyle='-', linewidth=2, label=f'Média = {media_med_jul:.2f}')

        ax.axhspan(ic_min_med_jul, ic_max_med_jul, color='gray', alpha=0.3, label='IC 95%')

        # Adiciona rótulos e título
        ax.set_xlabel("Índice")
        ax.set_ylabel("Medição de Julho")
        ax.set_title("Comparação com Intervalo de Confiança")
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)

    st.markdown("""
    <style>
        .justificado {
            text-align: justify;
        }
    </style>

    <br>
    <p class="justificado">
    Para entender melhor os dados analisados, foram calculados os <b>intervalos de confiança de 95%</b> para algumas variáveis importantes relacionadas à precipitação em julho nas estações de Ribeirão Preto.
    </p>

    <p class="justificado">
    O intervalo de confiança é uma faixa de valores onde temos uma alta probabilidade de que esteja a média real da variável analisada. No nosso caso, esse intervalo nos diz onde provavelmente está o valor verdadeiro da média de precipitação, com 95% de confiança.
    </p>

    <p class="justificado">
    Por exemplo, se a média de precipitação em julho (MED_JUL) for 42,7 mm, com um intervalo de confiança entre 39,5 mm e 45,9 mm, isso significa que podemos afirmar, com 95% de certeza, que a média real está dentro desse intervalo.
    </p>

    <p class="justificado">
    Esse tipo de análise ajuda a entender melhor a <b>confiabilidade dos dados</b>, e também a <b>comparar diferentes períodos ou regiões</b> com base em medidas mais precisas. Assim, mesmo que os dados tenham alguma variação natural, conseguimos tomar decisões e tirar conclusões com mais segurança.
    </p>
    """,
    unsafe_allow_html=True)
    
    
