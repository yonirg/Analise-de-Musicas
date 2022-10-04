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

def musica_mais_tocada():
    #a partir do dataframe, é possível escolher a música mais tocada
    #as músicas estão ordenadas de acordo com as mais tocadas, de acordo com o site que realizamos o scraping
    print("A música mais tocada é", musica_tocada(1))
    df_musicas = pd.DataFrame(pega_musicas(), columns = ["Musicas"])
    df_ouvir = pd.DataFrame(pega_ouvir(), columns=["Numero_Ouvintes"])
    df_musicas.reset_index(drop=True, inplace=True)
    df_ouvir.reset_index(drop=True, inplace=True)
    df_faixas = pd.concat([df_musicas, df_ouvir], axis=1)
    print(df_faixas)
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

#musica_mais_tocada()
#musica_menos_tocada()

#print(musica_menos_tocada())

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
            print(f"Sem músicas no Álbum {nome_album}  Erro: {error}")
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
    coluna = "Palavras_Album"
    df_album = pd.DataFrame(lista_palavras, columns=[coluna])
    print(df_album.value_counts())
    texto = df_album.values
    return texto

def wordcloud_album(texto):
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
    coluna = "Palavras_Música"
    df_musica = pd.DataFrame(lista_palavras, columns=[coluna])
    print(df_musica.value_counts())
    texto = df_musica.values
    return texto

def wordloucd_musica(texto):
    wordcloud_musicas = WordCloud().generate(str(texto))
    plt.imshow(wordcloud_musicas)
    plt.axis("off")
    plt.show()
    return wordcloud_musicas

#musicas_mais_plv()

#Função que pega as letras das músicas únicas de todos os álbuns
def pega_letras_unicas(data_frame_multiindex):
    new_df = data_frame_multiindex.reset_index()
    df_unicas = pd.DataFrame(new_df["Musica"].unique(), columns=["Musica"])
    lista_letras=[]
    for musica in df_unicas["Musica"]:
        musica_convertida = musica.lower().replace(" ", "-").replace("(", "").replace(')',"").replace("'", "").replace("/","")
        try:
            page = requests.get(f"https://www.letras.mus.br/imagine-dragons/{musica_convertida}/")
        except Exception as error:
            print(f"não foi possível buscar a letra da música {musica} devido a grande quantidade de redirecionamentos")
            print(f"Erro: {error}")
            letra = "SEM LETRA"
        else:
            soup = BeautifulSoup(page.content, "html.parser")
            with open("x.html","w", encoding="utf-8") as f:
                f.write(str(soup))
            letra = soup.find("div", class_= "cnt-letra p402_premium")
            letra = str(letra).replace('<div class="cnt-letra p402_premium">','').replace(" <p>", "").replace("<p>", " ").replace("</p>", "").replace("<br/>", " ").replace("<br>", " ").replace("</br>", "").replace("</div>", "")
        finally:    
            lista_letras.append(letra)
    df_unicas["Letra"] = lista_letras
    return df_unicas

# Função que a adiciona as letras ao dataframe com multiindex
def letras_df(df, df_unicas):
    df_unicas = df_unicas.set_index("Musica")
    left = df_unicas
    right = df
    result = left.join(right, how="inner")
    return result

#função que gera o multiindex
def musica_com_letras():
    arrays = auxiliar_multi_index(albuns_musicas())
    df = df_MI(arrays)
    df_unicas = pega_letras_unicas(df)
    df_final = letras_df(df, df_unicas)
    return df_final

#função que mostra o número de palavras nas letras das músicas e suas quantidades
def letras_mais_plv():
    letras = (musica_com_letras().reset_index())
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

print(letras_mais_plv())

#função que gera um wordcloud a partir do número de palavras das músicas
def letras_wordcloud():
    df_letras = letras_mais_plv()
    print(df_letras.value_counts())
    texto = df_letras.values
    wordcloud_letras = WordCloud().generate(str(texto))
    plt.imshow(wordcloud_letras)
    plt.axis("off")
    plt.show()
    return wordcloud_letras

letras_wordcloud()

def pega_premios():
    premios = []
    page = requests.get("https://www.imdb.com/name/nm4995251/awards?ref_=nm_awd")
    soup = BeautifulSoup(page.content, "html.parser")
    container_premios = soup.find_all("td", class_ = "award_outcome")
    with open("x.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
    for award in container_premios:
        premios.append(award.find_all("span", class_ = "award_category")[0].get_text())
    df_premios = pd.DataFrame(premios, columns=["Prêmios"])
    return df_premios

#print(pega_premios())

def pega_vencedor():
    vencedor = []
    page = requests.get("https://www.imdb.com/name/nm4995251/awards?ref_=nm_awd")
    soup = BeautifulSoup(page.content, "html.parser")
    container_vencedor = soup.find_all("td", class_ = "award_outcome")
    with open("x.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
    for award in container_vencedor:
        vencedor.append(award.find_all("b")[0].get_text())
    df_vencedor = pd.DataFrame(vencedor, columns=["Vencedor"]) 
    return df_vencedor

#print(pega_vencedor())

def numero_vencedor():
    pega_premios().reset_index(drop=True, inplace=True)
    pega_vencedor().reset_index(drop=True, inplace=True)
    vencedor_premio = pd.concat([pega_premios(),pega_vencedor()], axis=1)
    numero_premio = vencedor_premio[vencedor_premio.Vencedor=="Winner"].value_counts()
    return numero_premio

#print(album_vencedor())

# ### ÁREA DE TESTE

def musica_com_letras():
    arrays = auxiliar_multi_index(albuns_musicas())
    df = df_MI(arrays)
    df_unicas = pega_letras_unicas(df)
    df_final = letras_df(df, df_unicas)
    return df_final

#musica_com_letras()

#função que retorna o número de palavras das músicas, por álbum
def letras_por_album():
    df_musica_letras = musica_com_letras()
    excecoes = ["Origins (Deluxe)", "Demons (TELYKast Remix)", "Shots (The Funk Hunters Remix)", "Shots (AtellaGali Remix)", "Mercury - Act 1 (Amazon Music Live)", "It's Time (Single Of The Week)", "Clouds (2008 Version) [Demo]"]
    for album in pega_albuns():
        if album in excecoes:
            print(f"o {album} não possui músicas contidas dentro dele")
            pass
        else:
            df_musica_album = df_musica_letras.loc[album, :]
            letra = (str(df_musica_album.loc[:, "Letra"])).split(" ")
            filtro =  ["-", "\ ", "(",")", "/", "]", "[", " \ ", "'", '"', "+", "_"," ", ",", ";", "\n", "\t", "...\nName:"]
            for i in letra:
                if i == filtro:
                    letra.remove(i)
            df_letras = pd.DataFrame(letra, columns=["Letra"])
            df_contar = df_letras.value_counts()
            print("\n\n",album, df_contar.iloc[1: ], "\n\n", "_"*40)
        pd.set_option("display.max_rows", 10)
        pd.set_option("display.max_columns", 10)
    return

#letras_por_album()

def album_in_letras():
    df_letras = letras_mais_plv() 
    lista_album = str(pega_albuns()).split
    df_album_in_letras = df_letras[df_letras["letras"]==lista_album]
    return df_album_in_letras

#print(letras_mais_plv())


def musicas_in_letras():
    return