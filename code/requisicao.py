import requests
import xml.etree.ElementTree as ET
import pandas as pd

def coletar_noticias(termo_busca):
    url = f"https://news.google.com/rss/search?q={termo_busca}&hl=pt-BR&gl=BR&ceid=BR:pt-419"



    try:
        response = requests.get(url)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        channel = root.find("channel")
        dados_noticias = []

        if channel is not None:
            for item in channel.findall("item"):
                titulo = item.find('title').text
                link = item.find('link').text
                descricao = item.find('description').text

                dados_noticias.append({
                    'titulo' : titulo,
                    'link' : link,
                    'descricao' : descricao
                })
        return dados_noticias[:15]
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao coletar notícias: {e}")
        return []
    except ET.ParseError as e:
        print(f"Erro ao analisar XML: {e}")
        return []

termo = "inteligencia+artificial+no+piaui"
noticias = coletar_noticias(termo)

if noticias:
    df_noticias = pd.DataFrame(noticias)
    print(f"Quantidades de noticias coletadas: {len(df_noticias)}")
    print(df_noticias)
else:
    print("Nenhuma notícia encontrada.")





