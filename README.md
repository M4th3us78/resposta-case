# Case - Análise de sentimentos e identificação de temas recorrentes

Repositório desenvolvido com o intuito de realizar a análise de notícias no feed RSS do google notícias sobre Inteligência Artificial no Piauí.

# Objetivo

Analisar os sentimentos das notícias sobre o tema pesquisado.

# Como funciona

A aplicação realiza um pipeline completo:
1. **Coleta de Dados:** Utiliza o feed RSS do Google Notícias para buscar as últimas matérias sobre o tema.

2. **Processamento de Texto:** Limpa e normaliza os títulos das notícias.

3. **Análise de Sentimento:** Classifica cada notícia como positiva, negativa ou neutra com base em uma lista de palavras-chave.

4. **Visualização:** Apresenta os dados em um dashboard interativo construído com Streamlit, contendo gráficos e uma nuvem de palavras.


## Tecnologias Utilizadas

As seguintes ferramentas e bibliotecas foram utilizadas na construção do projeto:

-   **Linguagem:** Python 3.10
-   **Dashboard:** Streamlit
-   **Manipulação de Dados:** Pandas
-   **Requisições HTTP:** Requests
-   **Processamento de Texto:** WordCloud, Unidecode
-   **Visualização de Dados:** Plotly, Matplotlib

## Como executar o projeto

Siga as intruções abaixo para conseguir executar a aplicação.

## Pré-requisitos
-Python 3.10+ 

-Git


## Passos para Execução

1. **Clone o repositório**
    ```bash
    
    git clone https://github.com/M4th3us78/resposta-case

    cd resposta-case
    
2. **Crie e ative um ambiente virtual**
    ``` bash
    ## Para Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    ## Para Windows
    python -m venv venv
    .\venv\Scripts\activate

3. **Instale as dependências**
    ``` bash
    pip install -r requirements.txt


4. **Entre na pasta do projeto**
    ``` bash
    cd code/
    

4. **Execute o Dashboard Streamlit**
    ``` bash
    streamlit run app.py

Após executar o último comando, seu navegador abrirá automaticamentecom com o Dashboard.

## Download dos dados

Ao final da página haverá um botão disponibilizando o download do arquivo em formato CSV.