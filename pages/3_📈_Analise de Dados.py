import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import f

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
    
    
    st.write("")
    st.markdown(
        """
        <style>
            .justificado {
                text-align: justify;
            }
        </style>

        <p class="justificado">Para criar o gráfico e realizar os calculos referentes ao intervalo de confiança primeiro foi preciso juntar todos os valores das minimas, médias e máximas de todos os meses da base de dados, depois disso, definimos o limite superior como a maior das maximas, o limite inferior como a menor das mínimas e a média calculando a média das médias de cada mês</p>
        </br>
        
        <h2>Primeiras perguntas e Hipóteses</h2>
        <h3>Chuvas com volume variavel</h3>
        <p class="justificado">Pelo gráfico é possivel notar que os mêses mais chuvosos tem um erro maior porque as chuvas provavelmente são mais variaveis, ou seja, em alguns dias chove muito e em outros não chove ou chove bem pouco. Então o erro padrão é maior, porque se for observado um mês menos chuvoso como agosto o erro padrão é menor, possivelmente por ter chuvas menos volumosas.</p>
        </br>
        <h3>Chuvas em mais ou menos dias</h3>
        <p class="justificado">Outra hipótese é que os mêses menos chuvosos do ano tem um erro padrão menor por terem menos dados, por exemplo, enquanto em dezembro choveu em 20 dias do mês, em agosto só choveu apenas em 9, consequentemente é observada uma variância menor</p>       
        """,
        unsafe_allow_html=True
        )
    
    st.write("")
    st.markdown(
        """
        <style>
            .justificado {
                text-align: justify;
            }
        </style>

        <h2>Testes de Hipótese</h2>
        <p class="justificado">Utilizando as hipóteses formadas anteriormente e formulando algumas novas, podemos conduzir os testes de hipótese:</p>
        """,
        unsafe_allow_html=True
        )
    subcol1, subcol2, subcol3 = st.columns([1, 7, 1])
    
    with subcol2:
        st.markdown('<h3>F-TEST</h3>',unsafe_allow_html= True)
        st.write("Hipótese H₀: As variâncias são iguais")
        st.latex("H₀: σ²_{JAN} = σ²_{AGO}")

        st.write("")
        st.write("Hipótese H₁: A variância de janeiro é maior")
        st.latex("H₁: σ²_{JAN} > σ²_{AGO}")

        st.latex(r'''F = \frac{S_{\mathrm{JAN}}^2}{S_{\mathrm{AGO}}^2}''')

        jan_np = df_rp[['MIN_JAN', 'MED_JAN', 'MAX_JAN']].values.flatten().tolist()
        ago_np = df_rp[['MIN_AGO', 'MED_AGO', 'MAX_AGO']].values.flatten().tolist()

        # Calcular variâncias
        var1 = np.var(jan_np, ddof=1)
        var2 = np.var(ago_np, ddof=1)

        # Estatística F
        F = var1 / var2

        # Graus de liberdade
        df1 = len(jan_np) - 1
        df2 = len(ago_np) - 1

        # p-valor
        p_value = 1 - f.cdf(F, df1, df2)

        # Exibir

        st.markdown('<h4>Resultados:</h4>', unsafe_allow_html=True)
        st.markdown(f'<span style="color:red;">Estatística F: {F:.2f}</span>', unsafe_allow_html=True)
        st.markdown(f'<span style="color:red;">P-valor: {p_value:.4f}</span>', unsafe_allow_html=True)

        st.markdown(
            """
            <style>
                .justificado {
                    text-align: justify;
                }
            </style>
            <p class="justificado">Com base nos resultados obtidos, a Estatística F foi calculada como 18.71, com um p-valor de 0.0000. Isso significa que o p-valor é extremamente baixo, indicando que existe uma diferença estatisticamente significativa entre as variâncias de janeiro e agosto.</p>
            <p class="justificado">Como o p-valor é muito menor do que o nível de significância comum (como 0.05 ou 0.01), rejeitamos a hipótese nula (H₀). Ou seja, podemos concluir que a variância de janeiro é significativamente maior do que a variância de agosto, conforme sugerido pela hipótese alternativa (H₁).</p>
            """,
            unsafe_allow_html=True
            )
        
        st.title("")
        st.markdown('<h3>Teste de proporção ou Z-TEST</h3>',unsafe_allow_html= True)
        st.write("Hipótese H₀: A proporção de dias com chuva é igual entre agosto e dezembro")
        st.latex("H₀: p₁ = p₂")

        st.write("")
        st.write("Hipótese H₁: Dezembro tem mais dias com chuva")
        st.latex("H₁: p₁ > p₂")
        
        st.latex(r'''Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0 (1 - p_0)}{n}}}''')
        
        proporcao1 = df_rp[['MIN_DEZ']].values.flatten().tolist()
        proporcao2 = df_rp[['MIN_AGO']].values.flatten().tolist()
        
        st.markdown(
            """
            <style>
                .justificado {
                    text-align: justify;
                }
            </style>
            <p class="justificado">Nesse caso, só queremos comparar os dias sem chuva, então só precisamos das mínimas das estações (MIN_AGO, MIN_DEZ)</p>""",
            unsafe_allow_html=True
            )
        
        
        def proporcao(proporcao):
            return sum(1 for x in proporcao if x != 0)
        
        count_dez = proporcao(proporcao1)
        count_ago = proporcao(proporcao2)
        
        st.write(f"Nas 6 estações de ribeirão preto a quantidade de minimas diferentes de 0 em dezembro:{count_dez}")
        st.write(f"Nas 6 estações de ribeirão preto a quantidade de minimas diferentes de 0 em agosto:{count_ago}")
        
        n = 6

        # Proporções
        p_hat = count_dez / n
        p0 = count_ago / n

        # Estatística Z
        z = (p_hat - p0) / np.sqrt((p0 * (1 - p0)) / n)

        # P-valor (teste unilateral: p_hat > p0)
        p_value2 = 1 - norm.cdf(z)
        
        st.write("")
        st.markdown('<h4>Resultados:</h4>', unsafe_allow_html=True)
        st.markdown(f'<span style="color:red;">Estatística Z: {z:.2f}</span>', unsafe_allow_html=True)
        st.markdown(f'<span style="color:red;">P-valor: {p_value2:.4f}</span>', unsafe_allow_html=True)
        
        st.markdown(
            """
            <style>
                .justificado {
                    text-align: justify;
                }
            </style>
            <p class="justificado">Dado que o p-valor obtido é significativamente menor que o nível de significância convencional (α=0,05), rejeita-se a hipótese nula. Isso indica que há evidências estatísticas suficientes para afirmar que a proporção de dias com chuva no mês de dezembro é significativamente maior do que no mês de agosto, considerando os dados das estações de Ribeirão Preto analisadas.</p>
            """,
            unsafe_allow_html=True
            )
    
    
    
    
    
    