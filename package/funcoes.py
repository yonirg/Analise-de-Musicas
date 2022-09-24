#Importe as bibliotecas e módulos necessários
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Função que pega todas as músicas do Imagine Dragons
def pega_musicas():
    musicas = []
    i=1
    while i<=10:
        page = requests.get(f"https://www.last.fm/pt/music/Imagine+Dragons/+tracks?page={i}")
        soup = BeautifulSoup(page.content, 'html.parser')
        container_musicas =soup.find_all('td', class_='chartlist-name')
        for musica in container_musicas:
            musicas.append(musica.find_all('a')[0].get_text())
        i+=1
