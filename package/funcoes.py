#Importe as bibliotecas e módulos necessários
from modulefinder import STORE_GLOBAL
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import quote_plus
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import  WordCloud
import sys
import seaborn as sns

np.set_printoptions(threshold=sys.maxsize)

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", 10)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

# Função que pega todas as músicas do Imagine Dragons
def pega_musicas():
    musicas = []
    i=1
    while i<=10:
        page = requests.get(f"https://www.last.fm/pt/music/Imagine+Dragons/+tracks?page={i}")
        soup = BeautifulSoup(page.content, "html.parser")
        container_musicas = soup.find_all("td", class_= "chartlist-name")
        for musica in container_musicas:
            musicas.append(musica.find_all("a")[0].get_text())
        i+=1
    return musicas

#criando uma função para printar o número de ouvintes, porém, estou tendo problemas com filtragem - RESOLVER ISSO DEPOIS URGENTEMENTE
def pega_views():
    visualizacoes = []
    i = 1
    while i <= 10:
        page = requests.get(f"https://www.last.fm/pt/music/Imagine+Dragons/+tracks?page={i}")
        soup = BeautifulSoup(page.content, "html.parser")
        container_visualizacoes = soup.find_all("td", class_ = "chartlist-bar")
        for view in container_visualizacoes:
            visualizacoes.append(int(view.find_all("span", class_ = "chartlist-count-bar-value")[0].get_text().replace("\n", "").replace(" ", "").replace("ouvintes", "").replace(".", "")))
        i+=1
    df_ouvir = pd.DataFrame(visualizacoes, columns=["Numero_Ouvintes"])
    return df_ouvir


print(pega_views())


#criando um dataframe que pega todas as músicas do scraping e as ordenam
df = pd.DataFrame(pega_musicas(), columns = ["Músicas"])
#as músicas estão ordenadas de acordo com as mais tocadas, de acordo com o site que realizamos o scraping

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
            musica_tocada = df["Músicas"].iloc[n-1]
            return(musica_tocada)
        #localiza o índice da função
    except Exception as error:
        return error

#musica_tocada(-1)

def musica_mais_tocada():
    #a partir do dataframe, é possível escolher a música mais tocada
    print("A música mais tocada é", musica_tocada(1))
    return

def musica_menos_tocada():
    #a partir do dataframe, é possível escolher a música menos tocada
    df_musicas_inv = df_musicas.tail(1)
    print("A música menos tocada é",df_musicas_inv["Músicas"].iloc[0])
    return

#musica_mais_tocada ()
#musica_menos_tocada()

#Função que pega todos os álbuns da Imagine Dragons
def pega_albuns():
    albuns = []
    i=1
    while i<=7:
        page = requests.get(f"https://www.last.fm/pt/music/Imagine+Dragons/+albums?page={i}")
        soup = BeautifulSoup(page.content, "html.parser")
        container_albuns = soup.find(id="artist-albums-section").find_all(class_="link-block-target")
        for album in container_albuns:
            albuns.append(album.get_text())
        i+=1
    return albuns


def albuns_musicas():
    dict_albuns_musicas = {}
    for nome_album in pega_albuns():
        if "+" in nome_album:
            nome_album = nome_album.replace("+", "%2B")
        album_codificado = quote_plus(nome_album)
        page = requests.get(f"https://www.last.fm/pt/music/Imagine+Dragons/{album_codificado}")
        soup = BeautifulSoup(page.content, "html.parser")
        try:
            container_musicas_album = soup.find("section", id= "tracklist").find("tbody")
        except AttributeError as error:
            print("Sem músicas nesse Álbum", error)
            continue
        musicas_album = container_musicas_album.find_all('tr')
        conjunto_musicas_album = []
        for musica_album in musicas_album:
            nome_musica = musica_album.find("td", class_="chartlist-name").find("a").get_text()
            conjunto_musicas_album.append(nome_musica)
        if "%2B" in nome_album:
            nome_album = nome_album.replace("%2B", "+")
        dict_albuns_musicas[nome_album]=conjunto_musicas_album
    return dict_albuns_musicas

def auxiliar_multi_index(dict_albuns_musicas):
    lista_index1 = []
    for item in dict_albuns_musicas:
        for vezes in range(len(dict_albuns_musicas[item])):
            lista_index1.append(item)
    lista_index2 = []
    for chave in dict_albuns_musicas:
        lista_index2 += dict_albuns_musicas[chave]    
    arrays = [lista_index1, lista_index2]
    return arrays

#Cria DataFrame com  MultiIndex
def df_MI(arrays):
    multi_index = pd.MultiIndex.from_arrays(arrays, names=('Album', 'Musica'))
    df = pd.DataFrame(index=multi_index)
    return df

#arrays = auxiliar_multi_index(albuns_musicas())
#df = df_MI(arrays)
#print(df)

#função para transformar album em dataframe
def albuns_mais_plv():
    palavras = str(pega_albuns()).split()
    lista_palavras = []
    for a in palavras:
        item = a
        for b in ["-", "\ ", "(",")", "/", "]", "[", " \ ", "'", '"', "+", "_"," ", ",", ""]:
            item = item.replace(b, "")
        lista_palavras.append(item)
    for a in lista_palavras:
        if a == "":
            lista_palavras.remove(a)
    coluna = "Album"
    df_album = pd.DataFrame(lista_palavras, columns=[coluna])
    print(df_album.value_counts())
    texto = df_album.values
    wordcloud = WordCloud().generate(str(texto))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    return wordcloud

#albuns_mais_plv()

def musicas_mais_plv():
    palavras = str(pega_musicas()).split()
    lista_palavras = []
    for a in palavras:
        item = a
        for b in ["-", "\ ", "(",")", "/", "]", "[", " \ ", "'", '"', "+", "_"," ", ",", ";"]:
            item = item.replace(b, "")
        lista_palavras.append(item)
    for a in lista_palavras:
        if a == "":
            lista_palavras.remove(a)
    coluna = "Musica"
    df_musica = pd.DataFrame(lista_palavras, columns=[coluna])
    print(df_musica.value_counts())
    texto = df_musica.values
    wordcloud = WordCloud().generate(str(texto))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    return wordcloud

#musicas_mais_plv()
