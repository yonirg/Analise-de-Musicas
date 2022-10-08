import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
import sys
print(sys.path)
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import pathlib
import numpy as np
import re
from urllib.parse import quote_plus


caminho_dataset = sys.path[0].replace("perguntas_etapa_2", "dataset_etapa_1")
sys.path.insert(0, caminho_dataset)
from dataframes_prontos import dataset_com_ouvintes,dataframe
# caminho = pathlib.Path()
# for pasta in caminho:
#     print(pasta)
#print(caminho)
#from modulo_dataset import pega_albuns


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

#função utilizada para resolevr o problema de Unicode
def printRAW(*texto):
    RAWOut = open(1, "w", encoding="utf8", closefd=False)
    print(*texto, file=RAWOut)
    RAWOut.flush()
    RAWOut.close()
    return

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

def letras_df(df, df_unicas):
    df_unicas = df_unicas.set_index("Musica")
    left = df_unicas
    right = df
    result = left.join(right, how="inner")
    return result

def musica_com_letras():
    arrays = auxiliar_multi_index(albuns_musicas())
    df = df_MI(arrays)
    df_unicas = pega_letras_unicas(df)
    df_final = letras_df(df, df_unicas)
    return df_final


######################################## GRUPO 1 DE PERGUNTAS ########################################


#PERGUNTA 1
# Retorna um dicionário de até as 5 músicas mais ouvidas por álbum
def mais_ouvintes_por_album(dataset_com_ouvintes, dataframe):
    dict_mais_ouvidas = {}
    dataset_com_ouvintes = dataset_com_ouvintes[dataset_com_ouvintes.Ouvintes != "Nan"]
    dataset_com_ouvintes.dropna(inplace=True)
    dataset_com_ouvintes["Ouvintes"] = dataset_com_ouvintes["Ouvintes"].astype(int)
    dataset_com_ouvintes['Ouvintes_sem_nulos']=dataset_com_ouvintes.Ouvintes.apply(lambda x: np.where(str(x).isdigit(),x,'0'))
    for album in dataframe.reset_index()["Album"].unique():
        ouvintes_musicas = dataset_com_ouvintes.loc[album]["Ouvintes_sem_nulos"]
        nome_musica = ouvintes_musicas.astype(int).sort_values(ascending=False).index.values[:5]
        num_ouvintes = ouvintes_musicas.astype(int).sort_values(ascending=False).iloc[:5]
        dicionario_musicas = {}
        i=0
        while i<= len(nome_musica)-1:
            dicionario_musicas[nome_musica[i]] = num_ouvintes[i]
            i+=1
        dict_mais_ouvidas[album] =dicionario_musicas
    return dict_mais_ouvidas

def grafico_mais_ouvinte_por_album(dict_mais_ouvidas):
    df = pd.DataFrame.from_dict(dict_mais_ouvidas, orient="index").stack().to_frame()
    df = pd.DataFrame(df[0].values.tolist(), index = df.index)
    df = str(df.values.tolist()).split()
    lista=[]
    for valor in df:
        valor=re.sub(r"[$/\]","",valor)
        lista.append(valor)
    filtro = re.compile("[\w+]")
    lista = list(filter(filtro.match, df))
    return lista
    

print(grafico_mais_ouvinte_por_album(mais_ouvintes_por_album(dataset_com_ouvintes, dataframe)))



# Retorna um dicionário de até as 5 músicas menos ouvidas por álbum
def menos_ouvintes_por_album(dataset_com_ouvintes, dataframe):
    dict_menos_ouvidas = {}
    dataset_com_ouvintes = dataset_com_ouvintes[dataset_com_ouvintes.Ouvintes != "Nan"]
    dataset_com_ouvintes.dropna(inplace=True)
    dataset_com_ouvintes["Ouvintes"] = dataset_com_ouvintes["Ouvintes"].astype(int)
    dataset_com_ouvintes = dataset_com_ouvintes[dataset_com_ouvintes.Ouvintes != 0]
    dataset_com_ouvintes['Ouvintes_sem_nulos']=dataset_com_ouvintes.Ouvintes.apply(lambda x: np.where(str(x).isdigit(),x,'0'))
    for album in dataframe.reset_index()["Album"].unique():
        ouvintes_musicas = dataset_com_ouvintes.loc[album]["Ouvintes_sem_nulos"]
        nome_musica = ouvintes_musicas.astype(int).sort_values(ascending=True).index.values[:5]
        num_ouvintes = ouvintes_musicas.astype(int).sort_values(ascending=True).iloc[:5]
        dicionario_musicas = {}
        i=0
        while i<= len(nome_musica)-1:
            dicionario_musicas[nome_musica[i]] = num_ouvintes[i]
            i+=1
        dict_menos_ouvidas[album] =dicionario_musicas
    return dict_menos_ouvidas

# PERGUNTA 2
# Retorna um dicionário de até as 5 músicas mais curtas por álbum
def mais_curtas_por_album(dataset_com_ouvintes, dataframe):
    dict_mais_curtas = {}
    dataset_com_ouvintes.rename(columns={"Duracao(seg)": "Duracao"}, inplace=True)
    dataset_com_ouvintes['Duracao_sem_nulos']=dataset_com_ouvintes.Duracao.apply(lambda x: np.where(str(x).replace(".", "", 1).isdigit(),x,'0'))
    for album in dataframe.reset_index()["Album"].unique():
        ouvintes_musicas = dataset_com_ouvintes.loc[album]["Duracao_sem_nulos"]
        nome_musica = ouvintes_musicas.astype(float).sort_values(ascending=True).index.values[:5]
        num_ouvintes = ouvintes_musicas.astype(float).sort_values(ascending=True).iloc[:5]
        dicionario_musicas = {}
        i=0
        while i<= len(nome_musica)-1:
            dicionario_musicas[nome_musica[i]] = num_ouvintes[i]
            i+=1
        dict_mais_curtas[album] =dicionario_musicas
    return dict_mais_curtas


# Retorna um dicionário de até as 5 músicas mais longas por álbum
def menos_curtas_por_album(dataset_com_ouvintes, dataframe):
    dict_menos_curtas = {}
    dataset_com_ouvintes.rename(columns={"Duracao(seg)": "Duracao"}, inplace=True)
    dataset_com_ouvintes['Duracao_sem_nulos']=dataset_com_ouvintes.Duracao.apply(lambda x: np.where(str(x).replace(".", "", 1).isdigit(),x,'0'))
    for album in dataframe.reset_index()["Album"].unique():
        ouvintes_musicas = dataset_com_ouvintes.loc[album]["Duracao_sem_nulos"]
        nome_musica = ouvintes_musicas.astype(float).sort_values(ascending=False).index.values[:5]
        num_ouvintes = ouvintes_musicas.astype(float).sort_values(ascending=False).iloc[:5]
        dicionario_musicas = {}
        i=0
        while i<= len(nome_musica)-1:
            dicionario_musicas[nome_musica[i]] = num_ouvintes[i]
            i+=1
        dict_menos_curtas[album] =dicionario_musicas
    return dict_menos_curtas



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
    plt.show(block=False)
    plt.pause(6)
    plt.close()
    plt.savefig("musicas_mais_tocadas")
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
    plt.show(block=False)
    plt.pause(6)
    plt.close()
    plt.savefig("musicas_menos_tocadas")
    return barras 




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
    filtro=re.compile("[\w+]")
    lista = list(filter(filtro.match, lista_palavras))
    df_album = pd.DataFrame(lista, columns=[coluna])
    palavras_mais_comuns = df_album.value_counts()
    texto = df_album.values
    printRAW(palavras_mais_comuns)
    return texto

def wordcloud_album(texto):
    wordcloud = WordCloud().generate(str(texto))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show(block=False)
    plt.pause(6)
    plt.close()
    plt.savefig("palavras_mais_comuns_nos_albuns")
    return ""

#PERGUNTA 2
def musicas_mais_plv():
    palavras = str(pega_musicas()).split()
    lista_palavras = []
    for a in palavras:
        item = re.sub("[^A-Za-z0-9]+", "", a)
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



#PERGUNTA 3
def letras_por_album():
    df_musica_letras = musica_com_letras()
    excecoes = ["Origins (Deluxe)", "Demons (TELYKast Remix)", "Shots (The Funk Hunters Remix)", "Shots (AtellaGali Remix)", "Mercury - Act 1 (Amazon Music Live)", "It's Time (Single Of The Week)", "Clouds (2008 Version) [Demo]"]
    for album in pega_albuns():
        if album in excecoes:
            print(f"o {album} não possui músicas contidas dentro dele")
            pass
        else:
            df_musica_letras = df_musica_letras.reset_index()
            df_musica_album = df_musica_letras.loc[album, :]
            letra = list(str(df_musica_album.loc[:, "Letra"]).split(" "))
            filtro =  re.compile("/w+")
            letra = list(filter(filtro.match, letra))
            df_letras = pd.DataFrame(letra, columns=["Letra"]).drop_duplicates(subset=["Album"], keep=False)
            df_contar = df_letras.value_counts()
            print("\n\n",album.encode("utf-8"), df_contar.iloc[1: ], "\n\n", "_"*40)
        pd.set_option("display.max_rows", 10)
        pd.set_option("display.max_columns", 10)
    return

# PERGUNTA 4

def letras_mais_plv():
    letras = (musica_com_letras().reset_index())
    letras = np.array([letras.loc[:, "Letra"]])
    letras = str(list(letras)).split()
    lista=[]
    for a in letras:
        if a == r"\u0435":
            letras.replace(a, "")
        else:
            item = re.sub("[^A-Za-z0-9]+", "", a)
            lista.append(item)
    filtro =re.compile("[\w+]")
    lista = list(filter(filtro.match, lista))
    df_letras = pd.DataFrame(lista, columns=["Letra"])
    for value in df_letras.values:
        value = np.array(str(value).lower())
    print(df_letras.value_counts().iloc[0:30])
    return df_letras


def letras_wordcloud():
    df_letras = letras_mais_plv()
    np.set_printoptions(threshold=sys.maxsize)
    texto = df_letras.values
    wordcloud_letras = WordCloud().generate(str(texto))
    plt.show()
    plt.imshow(wordcloud_letras)
    plt.axis("off")
    plt.pause(6)
    plt.close()
    plt.savefig("palavras_mais_comuns_nas_letras")
    return wordcloud_letras

#letras_wordcloud()

# PERGUNTA 5

def letra_in_album():
    df_letras = letras_mais_plv() 
    lista_album = str(list(pega_albuns())).split
    df_letras = df_letras.isin([lista_album])
    df_album_in_letras = df_letras[df_letras["Letra"]==lista_album]
    return df_album_in_letras
#df.isin({'num_wings': [0, 3]})
#printRAW(pega_musicas())
#print(letra_in_album())
#printRAW(albuns_mais_plv()) #array

# PERGUNTA 6
def letra_in_musica():
    df_letras = letras_mais_plv() 
    lista_musica = str(pega_musicas()).split
    df_musica_in_letras = df_letras[df_letras["Letra"]==lista_musica]
    return df_musica_in_letras


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
