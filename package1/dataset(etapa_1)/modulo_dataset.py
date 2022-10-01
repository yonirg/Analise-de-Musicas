import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import quote_plus
import numpy as np


#Função que pega todos os álbuns da Imagine Dragons

def pega_albuns():
    albuns = []
    i=1
    while i<=7:
        page = requests.get(f"https://www.last.fm/pt/music/Imagine+Dragons/+albums?page={i}")
        soup = BeautifulSoup(page.content, "html.parser")
        container_albuns = soup.find(id="artist-albums-section").find_all(class_="link-block-target")
        with open("x.html","w", encoding="utf-8") as f:
            f.write(str(soup))
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
        with open("x.html","w", encoding="utf-8") as f:
            f.write(str(soup))
        try:
            container_musicas_album = soup.find("section", id= "tracklist").find("tbody")
        except AttributeError as error:
            #print(f"Sem músicas no Álbum {nome_album}  Erro: {error}")
            continue
        dict_albuns_musicas = auxiliar_albuns_musica(dict_albuns_musicas, container_musicas_album, nome_album)
    return dict_albuns_musicas


#Cria DataFrame vazio com  MultiIndex
def df_MI(arrays):
    multi_index = pd.MultiIndex.from_arrays(arrays, names=('Album', 'Musica'))
    df = pd.DataFrame(index=multi_index)
    return df


def pega_letras_unicas(data_frame_multiindex):
    new_df = data_frame_multiindex.reset_index()
    df_unicas = pd.DataFrame(new_df["Musica"].unique(), columns=["Musica"])
    lista_letras=[]
    for musica in df_unicas["Musica"]:
        musica_convertida = musica.lower().replace(" ", "-").replace("(", "").replace(')',"").replace("'", "").replace("/","")
        lista_letras = auxiliar_letras(musica, musica_convertida, lista_letras)
    df_unicas["Letra"] = lista_letras
    return df_unicas

# Adiciona as letras às músicas no dataframe multiindex
def letras_df(df, df_unicas):
    df_unicas = df_unicas.set_index("Musica")
    left = df_unicas
    right = df
    result = left.join(right, how="inner")
    return result



#*************************************************************** FUNÇÕES AUXILIARES***************************************************************#
def auxiliar_albuns_musica(dict_albuns_musicas, container_musicas_album, nome_album):
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


def auxiliar_letras(musica, musica_convertida, lista_letras):
    try:
        page = requests.get(f"https://www.letras.mus.br/imagine-dragons/{musica_convertida}/")
    except Exception as error:
        #print(f"não foi possível buscar a letra da música {musica} devido a grande quantidade de redirecionamentos")
        #print(f"Erro: {error}")
        letra = "SEM LETRA"
    else:
        soup = BeautifulSoup(page.content, "html.parser")
        with open("x.html","w", encoding="utf-8") as f:
            f.write(str(soup))
        letra = soup.find("div", class_= "cnt-letra p402_premium")
        letra = str(letra).replace('<div class="cnt-letra p402_premium">','').replace(" <p>", "").replace("<p>", " ").replace("</p>", "").replace("<br/>", " ").replace("<br>", " ").replace("</br>", "").replace("</div>", "")
    finally:    
        lista_letras.append(letra)
    return lista_letras