#Importe as bibliotecas e módulos necessários
from modulefinder import STORE_GLOBAL
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import quote_plus
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import sys
import seaborn as sns

np.set_printoptions(threshold=sys.maxsize)
'''
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", 10)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)
'''
# Função que pega todas as músicas do Imagine Dragons
def pega_musicas():
    musicas = []
    i=1
    while i<=10:
        page = requests.get(f"https://www.last.fm/pt/music/Imagine+Dragons/+tracks?page={i}")
        soup = BeautifulSoup(page.content, "html.parser")
        container_musicas = soup.find_all("td", class_= "chartlist-name")
        with open("x.html","w", encoding="utf-8") as f:
            f.write(str(soup))
        for musica in container_musicas:
            musicas.append(musica.find_all("a")[0].get_text())
        i+=1
    return musicas
#criando uma função para printar o número de ouvintes, porém, estou tendo problemas com filtragem
def pega_ouvir():
    ouvintes = []
    i = 1
    while i <= 10:
        page = requests.get(f"https://www.last.fm/pt/music/Imagine+Dragons/+tracks?page={i}")
        soup = BeautifulSoup(page.content, "html.parser")
        with open("x.html","w", encoding="utf-8") as f:
            f.write(str(soup))
        container_ouvintes = soup.find_all("td", class_ = "chartlist-bar")
        for ouvinte in container_ouvintes:
            ouvintes.append(int(ouvinte.find_all("span", class_ = "chartlist-count-bar-value")[0].get_text().replace("\n", "").replace(" ", "").replace("ouvintes", "").replace(".", "")))
        i+=1
    df_ouvir = pd.DataFrame(ouvintes, columns=["Numero_Ouvintes"])
    return df_ouvir

#print(pega_ouvir())

#criando uma função para printar a música referente a determinado índice, coloca o número da posiçãod a música, e a função mostrará
#Ex: caso eu queira escolher a música mais tocada, n = 1
def musica_tocada(n):
    try:
        if type(n) == float:
            raise TypeError("o número da música não pode ser em decimal")
        if n > 500:
            raise ValueError("não há mais de 500 músicas, escolha um número menor")
        elif n < 1:
            raise ValueError("o número de músicas não pode ser nulo ou negativo")
        else:
            df_musicas = pd.DataFrame(pega_musicas(), columns = ["Músicas"])
            musica_tocada = df_musicas["Músicas"].iloc[n-1]
            return(musica_tocada)
        #localiza o índice da função
    except Exception as error:
        return error

#musica_tocada(10)



#musica_mais_tocada()
#musica_menos_tocada()

#print(musica_menos_tocada())

#Função que pega todos os álbuns da Imagine Dragons









#Função que pega as letras das músicas únicas de todos os álbuns


# Função que a adiciona as letras ao dataframe com multiindex










# ### ÁREA DE TESTE
#arrays = auxiliar_multi_index(albuns_musicas())
#df = df_MI(arrays)
#df_unicas = pega_letras_unicas(df)
#df_final = letras_df(df, df_unicas)
#print(df_final)
