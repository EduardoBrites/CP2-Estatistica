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

st.sidebar.markdown("Desenvolvido por Eduardo Brites Coutinho")

st.title("Análise de dados")
st.title("")

col1, col2 = st.columns(2)


with col1:
    #st.markdown("<img src='img/D1/Home.png' style='widht: 100vw; display:flex; align-items: center; justify-content: center;'></img>", unsafe_allow_html=True)
    subcol1, subcol2, subcol3 = st.columns([1, 3, 5])
    with subcol2:
        st.image("img/Profile/gentrop_logo.jfif", width=100)
        
    with subcol3:
        st.title("Gentrop")
        st.write("")
        st.write("")
        st.write("")

secondarycol1, secondarycol2, secondarycol3 = st.columns([1, 5, 1])

with secondarycol2:        
    
    st.markdown(
    """
    <style>
    .justificado {
        text-align: justify;
    }
    </style>
    
    <h2>Sobre a gentrop?</h2>
    <p class="justificado">
        A Gentrop é uma empresa fundada em 2017, com operações no Brasil e na América Latina, especializada em impulsionar a inovação na nuvem e apoiar a transformação digital das empresas. Seu foco está na capacitação de pessoas e na promoção de mudanças culturais dentro das organizações.
    </p>
    <p class="justificado">
        Ao longo dos anos, a Gentrop consolidou um portfólio robusto de soluções em nuvem que abrangem segurança, colaboração, comunicação, gestão, marketing e vendas. Essas soluções são desenvolvidas em parceria com líderes tecnológicos como Google e Salesforce, permitindo que a Gentrop ofereça ferramentas avançadas para atender às necessidades específicas de seus clientes.
    </p>
    
    <h2>Base de dados</h2>
    <p class="justificado">
        Para essa análise uma pesquisa extensa foi feita para achar uma base de dados que possuisse porte para que ela fosse efetuada de maneira verossímil. O provedor da base é o TheirStack, uma ferramenta de vendas e marketing projetada para identificar clientes potenciais com base no uso de tecnologias e sinais de contratação. Ele rastreia mais de 7.000 tecnologias e analisa 50 milhões de ofertas de emprego em 100 países para fornecer insights sobre as stacks tecnológicas e necessidades de contratação das empresas.
    </p>
    <p class="justificado">
        Essa plataforma também oferece a opção de download dos dados procurados como um arquivo csv, ideal para ser analisado
    </p>
    """,
    unsafe_allow_html=True
    )
    st.title("")
    
col1, col2 = st.columns(2)

with col1:
    #st.markdown("<img src='img/D1/Home.png' style='widht: 100vw; display:flex; align-items: center; justify-content: center;'></img>", unsafe_allow_html=True)
    subcol1, subcol2, subcol3 = st.columns([1, 3, 5])
    with subcol2:
        st.image("img/Skills/SQL.png", width=100)
        
    with subcol3:
        st.title("Análise")
        st.write("")
        st.write("")
        st.write("")

secondarycol1, secondarycol2, secondarycol3 = st.columns([1, 5, 1])

with secondarycol2:
    
    st.markdown(
    """
    <h2>Visualização de todos os dados:</h2>
    """,
    unsafe_allow_html=True
    )
    
    st.write(df)
    st.write("")
    
    st.markdown(
    """
    <h2>Tipos de dados da base:</h2>
    
    <h3><strong>Variáveis Qualitativas</strong></h3>
    
    <p><strong>Variáveis nominais:</strong></p>
    <ul>
        <li>company_name</li>
        <li>company_url</li>
        <li>company_linkedin_url</li>
        <li>company_country</li>
        <li>company_country_code</li>
        <li>company_city</li>
        <li>company_industry</li>
        <li>company_seo_description</li>
        <li>company_description</li>
    </ul>

    <p><strong>Variáveis ordinais:</strong></p>
    <ul>
        <li>google-cloud-platform_confidence</li>
        <li>salesforce-marketing-cloud_confidence</li>
        <li>amazon-web-services_confidence</li>
        <li>google-drive_confidence</li>
        <li>onedrive_confidence</li>
    </ul>

    <h3><strong>Variáveis Quantitativas</strong></h3>

    <p><strong>Variáveis discretas:</strong></p>
    <ul>
        <li>company_employee_count</li>
        <li>technologies_count</li>
        <li>jobs_count</li>
    </ul>

    <p><strong>Variáveis contínuas:</strong></p>
    <ul>
        <li>company_founding_year</li>
        <li>jobs_titles</li>
        <li>annual_revenue_usd</li>
        <li>google-cloud-platform_n_jobs</li>
        <li>salesforce-marketing-cloud_n_jobs</li>
        <li>amazon-web-services_n_jobs</li>
        <li>google-drive_n_jobs</li>
        <li>onedrive_n_jobs</li>
    </ul>
    """,
    unsafe_allow_html=True
    )

    st.write("")
    
    st.markdown(
    """
    <h2>Perguntas feitas inicialmente:</h2>

    <h5>• O faturamento anual das empresas tem alguma relação com a quantidade de serviços de cloud que elas tem?</h5>   
    <br> 
    <h5>• Diferentes serviços de cloud impactam de maneiras diferentes a renda da empresa?</h5>
    <br>    
    <h5>• A quantidade de serviços de cloud adotados esta conectado com a quantidade de empregados na empresa?</h5>   
    """,
    unsafe_allow_html=True
    )
    
    st.title("")
    
    st.markdown(
    """
    <h2>Análise inicial dos dados:</h2> 
    
    """,
    
    unsafe_allow_html=True
    )

    st.write(df.describe())
    
    st.markdown(
    """
    <br>
    <h6>Fazendo uma análise inicial dos dados podemos análisar algumas coisas:</h6>
    <p>• A tecnologia que possui a maior média de serviços é a Amazon Web Services;</p>
    <p>• A tecnologia que possui o maior numero de vagasem uma só empresa é a Amazon Web Services;</p>
    <p>• A média de retorno financeiro das empresas está muito mais proxima do valor máximo do que do mínimo, o que nos indica que muitas empresas tem um bom retorno financeiro;</p>
    """,
    
    unsafe_allow_html=True
    )
    
    st.title("")
    
    st.markdown(
    """
    <h2>Respondendo as perguntas:</h2>

    <h5>• O faturamento anual das empresas tem alguma relação com a quantidade de serviços de cloud que elas tem?</h5>   
    <br> 
    """,
    unsafe_allow_html=True
    )
    
    cloud_columns = [
    'google-cloud-platform_n_jobs', 'salesforce-marketing-cloud_n_jobs',
    'amazon-web-services_n_jobs', 'google-drive_n_jobs', 'onedrive_n_jobs'
    ]

    # Verificando se todas as colunas estão no DataFrame antes de somar
    cloud_columns = [col for col in cloud_columns if col in df.columns]

    # Criando uma nova coluna para contar quantas tecnologias a empresa usa (1 a 5)
    df['cloud_presence_count'] = df[cloud_columns].gt(0).sum(axis=1)

    # Selecionando as primeiras 50 linhas e removendo onde "annual_revenue_usd" é null
    df_subset = df[['annual_revenue_usd', 'cloud_presence_count']].head(50).dropna(subset=['annual_revenue_usd'])

    st.markdown(
    """
    <style>
    .justificado {
        text-align: justify;
    }
    </style>
    
    <p class="justificado">Primeiramente, criamos uma nova coluna pra base que conta quantos serviços de cloud cada empresa usa, tambem eliminamos todas as empresas que não divulgaram a renda anual para não prejudicar a análise.</p>
    """,
    unsafe_allow_html=True
    )

    # Exibindo os dados
    st.write(df_subset)
    
    def format_func(value, tick_number):
        return f'{int(value):,}'

    plt.figure(figsize=(10, 5))
    plt.scatter(df_subset['annual_revenue_usd'], df_subset['cloud_presence_count'], alpha=0.5, color='b')
    plt.xlabel("Faturamento Anual (USD)")
    plt.ylabel("Quantidade de Serviços de Cloud")
    plt.title("Relação entre Faturamento e Uso de Cloud")

    from matplotlib.ticker import FuncFormatter
    
    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_func))

    plt.grid(True)

    st.markdown(
    """
    <p>Depois, plotamos o grafico para analisar. </p>
    """,
    unsafe_allow_html=True
    )
    st.pyplot(plt)
    
    df_filtered = df_subset[df_subset['annual_revenue_usd'] <= 5000000000]

    plt.figure(figsize=(10, 5))
    plt.scatter(df_filtered['annual_revenue_usd'], df_filtered['cloud_presence_count'], alpha=0.5, color='b')
    plt.xlabel("Faturamento Anual (USD)")
    plt.ylabel("Quantidade de Serviços de Cloud")
    plt.title("Relação entre Faturamento e Uso de Cloud")

    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_func))

    plt.grid(True)

    st.markdown(
    """
    <style>
    .justificado {
        text-align: justify;
    }
    </style>
    
    <p class="justificado">Como podemos observar existe um valor muito diferente dos demais, um outlier, pode ser um valor verídico, mas para podermos ver os outros com mais precisão removeremos ele por enquanto.</p>
    """,
    unsafe_allow_html=True
    )

    st.pyplot(plt)

    st.markdown(
    """
    <style>
    .justificado {
        text-align: justify;
    }
    </style>
    
    <p class="justificado">Com o que vemos nesse gráfico de cima nenhuma das empresas que divulgaram a renda anual tem menos do que dois serviços de cloud ou mais do que 4</p>
    <p class="justificado">A resposta para a pergunta que fizemos é, sim, ao analizar conseguimos perceber que as empresas que tem 3 serviços de cloud contratados recembem mais do que as que tem apenas dois, e as que possuem 4, por mais que sejam mais escassas também tem um faturamento anual maior.
    """,
    unsafe_allow_html=True
    )

    st.title("")
    
    st.markdown(
    """
    <h5>• Diferentes serviços de cloud impactam de maneiras diferentes a renda da empresa?</h5>   
    <br> 
    """,
    unsafe_allow_html=True
    )
    
    cloud_usage_counts = df[cloud_columns].gt(0).sum()

    st.write("Número de empresas que utilizam cada serviço de cloud:")
    st.write(cloud_usage_counts)

    mean_revenues_by_service = {}

    cloud_service_labels = [cloud_service.replace('_n_jobs', '') for cloud_service in cloud_columns]

    for cloud_service in cloud_columns:
        cloud_service_companies = df[df[cloud_service] > 0]
        mean_revenues_by_service[cloud_service] = cloud_service_companies['annual_revenue_usd'].mean()

    st.write("Média de faturamento anual por serviço de cloud:")
    st.write(mean_revenues_by_service)

    plt.figure(figsize=(10, 5))
    plt.bar(cloud_service_labels, mean_revenues_by_service.values(), color='b', alpha=0.7)

    plt.xlabel("Serviços de Cloud")
    plt.ylabel("Média de Faturamento Anual (USD)")
    plt.title("Média de Faturamento Anual por Serviço de Cloud")
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right')

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

    st.pyplot(plt)

    st.markdown(
    """
    <style>
    .justificado {
        text-align: justify;
    }
    </style>
    
    <p class="justificado">Analisando o gráfico e as tabelas acima é possivel observar que empresas que utilizam o salesforce possuem maior renda, porém é preciso levar em conta que 17 empresas utilizam salesforce, se essas mesmas empresas utilizarem outros serviços de cloud o valor final do salesforce aumenta</p>
    <p class="justificado">Logo em seguida temos Google Cloud e AWS como serviços de nuvem mais rentaveis para as empresas.</p>
    <p class="justificado">Respondendo a pergunta, sim, em um âmbito geral é possivel dizer que o serviço de cloud escolhido influencia diretamente na renda da empresa, porém sempre vale lembrar que as empresas apresentadas nessa base de dados não tem uma preferencia bem distribuida sobre os serviços de clous, o que leva alguns a serem menos populares que outros</p>
    """,
    unsafe_allow_html=True
    )

    st.title("")
    
    st.markdown(
    """
    <h5>• A quantidade de serviços de cloud adotados esta conectado com a quantidade de empregados na empresa?</h5>   
    <br> 
    """,
    unsafe_allow_html=True
    )
    
    bins = [0, 50, 100, 200, 500, 1000, 5000, 10000, np.inf]
    labels = ['0-50', '51-100', '101-200', '201-500', '501-1000', '1001-5000', '5001-10000', '10000+']

    
    df['employee_range'] = pd.cut(df['company_employee_count'], bins=bins, labels=labels)

    mean_cloud_by_range = df.groupby('employee_range')['cloud_presence_count'].mean()
    
    plt.figure(figsize=(10, 5))
    mean_cloud_by_range.plot(kind='bar', color='g', alpha=0.7)

    plt.xlabel("Número de Empregados")
    plt.ylabel("Média de Serviços de Cloud")
    plt.title("Relação entre Número de Empregados e Quantidade de Serviços de Cloud")
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

    st.pyplot(plt)

    st.markdown(
        """
        <style>
        .justificado {
            text-align: justify;
        }
        </style>

        <p class="justificado">O gráfico pode ajudar a visualizar se empresas maiores tendem a adotar mais serviços de cloud ou se não há uma correlação significativa.</p>
        <p class="justificado">Pelo gráfico é possivel observar que empresas que possuem três serviços de cloud contratados tem mais funcionários.</p>
        <p class="justificado">Respondendo a pergunta, não, não é possivel achar uma relação entre quantidade de serviços de cloud e numero de funcionarios, tendo em vista que empresas que possuem de 51-100 funcionários possuem apenas dois serviços de cloud, e empresas que possuem de 501-1000 também contratam 2. O que podemos afirmar é que, empresas que contratam 3 ou mais serviços de cloud tendem a ter mais funcionarios do que o resto. 
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
        
    <h2>Distribuição:</h2>
  
    <br>
    <p class="justificado">Para essa análise podemos utilizar a distribuição de Poisson para descobrir em um certo numero de eventos qual é a probabilidade de certa empresa ser escolhida</p>
    <p class="justificado">A baixo, escolhemos 50 como o numero de eventos desejado, representando o banco que tem 50 linhas de informação, em seguida definimos a taxa média de ocorrência, anteriormente no documento calculamos quantas empresas possuiam cada serviço de cloud, a tabela resultante foi a seguinte:</p> 
    """,
    unsafe_allow_html=True
    )
    
    st.write(cloud_usage_counts)
    
    st.markdown(
    """
    <style>
        .justificado {
            text-align: justify;
        }
    </style>
        
    <h2>Distribuição:</h2>
  
    <br>
    <p class="justificado">Se escolhermos, por exemplo o salesforce, devemos alterar a média de ocorrência para 17:""",
    unsafe_allow_html=True
    )
    
    def plot_distribution(x, y, title, xlabel, ylabel):
     fig = go.Figure(data=[go.Bar(x=x, y=y)])
     fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
     st.plotly_chart(fig)
    
    subcol1, subcol2 = st.columns([0.5, 0.5])
    
    lambd = subcol1.number_input("Taxa média de ocorrência (λ):",min_value=0.001,step=0.01,value=17.0)
    x_max = subcol1.number_input("Número de eventos desejado",min_value=0, step=1,value=50)
    x = np.arange(0, x_max)  
    y = stats.poisson.pmf(x, lambd)
    df_poisson = pd.DataFrame({"X": x, "P(X)": y, "P(X ≤ k) (Acumulado)": np.cumsum(y),
                               "P(X > k) (Acumulado Cauda Direita)": 1-np.cumsum(y)}).set_index("X")
    subcol2.write("Tabela de probabilidades:")
    subcol2.write(df_poisson)
    plot_distribution(x, y, "Distribuição de Poisson", "Número de eventos", "Probabilidade")
    
    st.title("")

    st.markdown(
    """
    <h2>Conclusão</h2>
    
    <p><strong>Relação entre faturamento e uso de cloud:</strong> A análise mostrou que existe, de fato, uma correlação entre o número de serviços de cloud adotados pelas empresas e o seu faturamento anual. Empresas que utilizam três ou mais serviços de cloud tendem a ter um faturamento mais alto, enquanto aquelas com dois serviços têm rendimentos mais baixos. Apesar de um outlier no conjunto de dados, a tendência geral é clara: a adoção de múltiplos serviços de cloud está associada a um melhor desempenho financeiro.</p>

    <p><strong>Impacto dos serviços de cloud na renda:</strong> A análise revelou que diferentes serviços de cloud impactam de maneiras distintas a renda das empresas. O Salesforce Marketing Cloud, por exemplo, apresentou uma média de faturamento anual significativamente maior, embora a sua popularidade seja menor. Já o Google Cloud e o AWS demonstraram uma relação forte com o aumento da receita. Isso sugere que a escolha do serviço de cloud pode ter um impacto direto no faturamento das empresas, mas é importante considerar a distribuição desigual de popularidade entre os serviços.</p>

    <p><strong>Relação entre número de empregados e uso de cloud:</strong> Em relação à quantidade de serviços de cloud adotados e o número de funcionários, a análise não encontrou uma correlação forte. Empresas de médio porte, com 51-100 funcionários, têm em média dois serviços de cloud, enquanto empresas maiores, com 501-1000 funcionários, também tendem a adotar apenas dois serviços. No entanto, empresas que utilizam três ou mais serviços de cloud tendem a ser mais numerosas em termos de funcionários.</p>

    <p>Em suma, a análise revelou que a adoção de múltiplos serviços de cloud pode ser uma estratégia eficaz para impulsionar o faturamento anual, mas não necessariamente leva a um aumento direto no número de empregados. Além disso, a escolha dos serviços de cloud deve ser cuidadosa, pois serviços como Salesforce, Google Cloud e AWS mostram ter um maior impacto financeiro, embora com diferentes níveis de adoção entre as empresas.</p>
    """,
    unsafe_allow_html=True
    )

    