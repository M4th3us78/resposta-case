import xml.etree.ElementTree as ET
import pandas as pd
import requisicao as req
import unicodedata as uni

def proces_sentimento(df):
    """Palavras selecionadas para tentar identificar os sentimentos da notícia (positivos e negativos)"""
    positivas = ["referencia","salto","avanço","revolucionar","revoluciona","amplia","ampliar","contribuir","contribui","fortalece","fortalece",
                "agilizar","capacitar","capacita","destaque","impulsiona","impulsionar","beneficios","modernizar","aprender","prepara","premiado",
                "inovar","inovacao","qualificar","desenvolvimento","inovacoes","lancamento","lanca"] 
    negativas = ['temida','negativamente','custo','consumo','riscos','incerta','desumanizar','ma','preucupa','contra','ameacam','perigoso','perigosa','degenerativa',
                 'inimiga','cuidado','substituir','alerta','desinformacao','prejudicar','reduzir','polemica']

    for titulo in df['titulo']:
        """Essa parte formatar o texto para poder comparar as palavras sem ocorrer erros"""
        texto_limpo = uni.normalize('NFD', titulo).encode('ascii', 'ignore').decode('utf-8')
        texto_limpo = texto_limpo.lower()

        """Cálculo simples para identificar o sentimento da notícia"""
        sent_positivo = 0
        sent_negativo = 0

        for palavra in positivas:
            if palavra in texto_limpo:
                sent_positivo += 1
        for palavra in negativas:
            if palavra in texto_limpo:
                sent_negativo += 1

        if sent_positivo > sent_negativo:
            df.loc[df['titulo'] == titulo, 'sentimento'] = 'positivo'
        elif(sent_positivo < sent_negativo):
            df.loc[df['titulo'] == titulo, 'sentimento'] = 'negativo'
        else:
            df.loc[df['titulo'] == titulo, 'sentimento'] = 'neutro'

    return df





