
import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
import sys
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import pathlib
import numpy as np
# caminho = pathlib.Path()
# for pasta in caminho:
#     print(pasta)
#print(caminho)
caminho_dataset = sys.path[0].replace("perguntas_etapa_2", "dataset_etapa_1")
sys.path.insert(0, caminho_dataset)
from modulo_dataset import pega_letras_unicas, df_MI, auxiliar_multi_index, albuns_musicas, pega_albuns


### GRUPO 1 DE PERGUNTAS


#PERGUNTA 1











# PERGUNTA 2










# PERGUNTA 3


def musica_mais_tocada():
    #a partir do dataframe, é possível escolher a música mais tocada
    #as músicas estão ordenadas de acordo com as mais tocadas, de acordo com o site que realizamos o scraping
    print("A música mais tocada é", musica_tocada(1))
    df_musicas = pd.DataFrame(pega_musicas(), columns = ["Musicas"])
    df_ouvir = pd.DataFrame(pega_ouvir(), columns=["Numero_Ouvintes"])
    df_musicas.reset_index(drop=True, inplace=True)
    df_ouvir.reset_index(drop=True, inplace=True)
    df_faixas = pd.concat([df_musicas, df_ouvir], axis=1)
    #print(df_faixas)
    df_faixas = df_faixas[0:5]
    barras = sns.barplot(x="Musicas", y="Numero_Ouvintes", data=df_faixas)
    plt.show()
    return barras

def musica_menos_tocada():
    #a partir do dataframe, é possível escolher a música menos tocada
    df_musicas = pd.DataFrame(pega_musicas(), columns = ["Musicas"])
    df_ouvir = pd.DataFrame(pega_ouvir(), columns=["Numero_Ouvintes"])
    df_musicas.reset_index(drop=True, inplace=True)
    df_ouvir.reset_index(drop=True, inplace=True)
    df_faixas = pd.concat([df_musicas, df_ouvir], axis=1)
    df_musicas_inv = df_musicas.tail(1)
    df_faixas_inv = df_faixas.tail(5)
    print("A música menos tocada é",df_musicas_inv["Musicas"].iloc[0])
    barras = sns.barplot(x="Musicas", y="Numero_Ouvintes", data=df_faixas_inv)
    plt.show()
    return barras 






# PERGUNTA 4






# PERGUNTA 5








# PERGUNTA 6



### GRUPO 2 DE PERGUNTAS

# PERGUNTA 1

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
    coluna = "Palavras_Album"
    df_album = pd.DataFrame(lista_palavras, columns=[coluna])
    palavras_mais_comuns = df_album.value_counts()
    texto = df_album.values
    return texto, palavras_mais_comuns


def wordcloud_album(texto):
    wordcloud = WordCloud().generate(str(texto))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show(block=False)
    plt.pause(6)
    plt.close()
    plt.savefig("palavras_mais_comuns_nos_albuns")
    return ""






# PERGUNTA 4
dict_albuns_musicas = albuns_musicas()

arrays = auxiliar_multi_index(dict_albuns_musicas)

dataframe = df_MI(arrays)

df_unicas = pega_letras_unicas(dataframe)

def letras_mais_plv():
    letras = (df_unicas.reset_index())
    letras = np.array([letras.loc[:, "Letra"]])
    letras = str(list(letras)).split()
    lista=[]
    for a in letras:
        if a == r"\u0435":
            letras.replace(a, "")
        elif a in [",",":","[","]",".",";","/","dtype=object","array",")","(","-"]:
            letras.replace(a, "")
        else:
            a.lower()
            lista.append(a)
    df_letras = pd.DataFrame(lista, columns=["Letra"])
    print(df_letras.value_counts().iloc[0:30])
    return df_letras
    

def letras_wordcloud():
    df_letras = letras_mais_plv()
    print(df_letras.value_counts())
    texto = df_letras.values
    wordcloud_letras = WordCloud().generate(str(texto))
    plt.show(block=False)
    plt.pause(6)
    plt.close()
    plt.savefig("palavras_mais_comuns_nas_letras")
    return wordcloud_letras



#*************************************************************** FUNÇÕES AUXILIARES***************************************************************#
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
