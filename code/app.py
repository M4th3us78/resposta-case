import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import processamento as proc
import requisicao as req
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


"""A busca dos dados"""
df = req.coleta()
df = proc.proces_sentimento(df)

st.set_page_config(layout="wide")
st.title("Painel de Monitoramento de Percepção sobre IA no Piauí.")

st.header("Notícias Coletadas")
st.dataframe(df[['titulo', 'sentimento']])

st.header("Análise de Sentimentos")
sent_cont = df['sentimento'].value_counts()
fig_pie = px.pie(
    values = sent_cont.values,
    names = sent_cont.index,
    title = "Distribuição de Sentimentos",
    color = sent_cont.index,
    color_discrete_map = {'Positivo':'green' , 'Negativo':'red' , 'Neutro':'blue'}
)
st.plotly_chart(fig_pie)

st.caption("Esta análise de sentimento é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos")


st.header("Nuvem de Palavras")
portuguese_stopwords = set(stopwords.words('portuguese'))

all_titles = ' '.join(df['titulo'])
wordcloud = WordCloud(max_words = 15,stopwords=portuguese_stopwords,width=800, height=400, background_color='white').generate(all_titles)

fig_wc, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig_wc)


st.header("Download dos Dados")
st.write("Clique no botão abaixo para baixar os dados em formato CSV.")
csv = df.to_csv(index=False)

st.download_button(
    label="Baixar arquivo CSV",
    data=csv,
    file_name="Notícias Coletadas.csv",
    mime="text/csv"
)

