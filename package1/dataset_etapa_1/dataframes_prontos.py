import os
import pandas as pd
import sys

atual = sys.path[0]
os.chdir(atual)

dataset_com_ouvintes = pd.read_csv("dataset_final.csv", index_col=[0,1])
dataframe = pd.read_csv("datafame_vazio_multiindex.csv", index_col=[0,1])
df_unicas = pd.read_csv("dataset_final.csv", index_col=[0,1])
dataframe_com_letras = pd.read_csv("dataframe_com_letras.csv")

