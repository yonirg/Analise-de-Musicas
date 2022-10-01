import pandas as pd
from urllib.parse import quote_plus
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup


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


### Venceram ou só foram nomeados
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
#### Prêmios vencidos e quantidade
def premio_vencedor():
    pega_premios().reset_index(drop=True, inplace=True)
    pega_vencedor().reset_index(drop=True, inplace=True)
    vencedor_premio = pd.concat([pega_premios(),pega_vencedor()], axis=1)
    vencedor_premio = vencedor_premio[vencedor_premio.Vencedor=="Winner"].value_counts()
    return vencedor_premio

print(premio_vencedor())

