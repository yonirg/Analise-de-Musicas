from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

def pega_albums():
    albums = []
    i = 1
    while i <= 10:
        page = requests.get(f"https://www.last.fm/pt/music/Imagine+Dragons/+albums?page={i}")
        soup = BeautifulSoup(page.content, "html.parser")
        print(soup)
    return albums

pega_albums()

