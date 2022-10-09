import pandas as pd
from urllib.parse import quote_plus
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

#QUANTAS NOMEAÇÕES A BANDA TEVE?
def pega_nomeacoes():
    nomeacao = []
    page = requests.get("https://www.imdb.com/name/nm4995251/awards?ref_=nm_awd")
    soup = BeautifulSoup(page.content, "html.parser")
    container_nomeacao = soup.find_all("td", class_ = "award_outcome")
    with open("x.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
    for award in container_nomeacao:
        nomeacao.append(award.find_all("span", class_ = "award_category")[0].get_text())
    df_nomeacao = pd.DataFrame(nomeacao, columns=["Prêmios"])
    df_nomeacao.value_counts()
    return df_nomeacao

print(pega_nomeacoes().value_counts())

#QUAIS FORAM OS ANOS QUE A BANDA MAIS GANHOU PRÊMIO?
def pega_ano_vencedor():
    vencedor = []
    page = requests.get("https://www.imdb.com/name/nm4995251/awards?ref_=nm_awd")
    soup = BeautifulSoup(page.content, "html.parser")
    container_vencedor = soup.find_all("table", class_ = "awards")
    with open("x.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
    for award in container_vencedor:
        vencedor.append(award.find_all("td")[0].get_text().replace("\n", "").replace(" ", ""))
    df_ano_vencedor = pd.DataFrame(vencedor, columns=["Ano Vencedor"]) 
    return df_ano_vencedor

print(pega_ano_vencedor().value_counts())

#QUAIS PREMIOS A BANDA GANHOU EM TODA SUA DISCOGRAFIA?
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

def numero_vencedor():
    pega_nomeacoes().reset_index(drop=True, inplace=True)
    pega_vencedor().reset_index(drop=True, inplace=True)
    vencedor_premio = pd.concat([pega_nomeacoes(),pega_vencedor()], axis=1)
    vencedor_premio = vencedor_premio[vencedor_premio.Vencedor=="Winner"].value_counts()
    return vencedor_premio

print(numero_vencedor())