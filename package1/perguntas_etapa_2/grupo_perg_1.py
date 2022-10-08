from turtle import clear
import funcoes as fun
import pandas as pd
import matplotlib.pyplot as plt
from dataframes_prontos import dataframe, dataset_com_ouvintes
from funcoes import premios_album
import seaborn as sns
# Resposta da pergunta 1

#Músicas com mais ouvintes por álbum:
print("\n\n\n\nMúsicas com mais ouvintes por álbum\n\n\n\n")
mais_ouvintes = fun.mais_ouvintes_por_album(dataset_com_ouvintes, dataframe)
print(mais_ouvintes)

#Músicas com menos ouvintes por álbum:
print("\n\n\n\nMúsicas com menos ouvintes por álbum\n\n\n\n")
menos_ouvintes = fun.menos_ouvintes_por_album(dataset_com_ouvintes, dataframe)
print(menos_ouvintes)






# Resposta da pergunta 2

#Músicas com mais duração por álbum:
print("\n\n\n\nMúsicas com mais duração por álbum\n\n\n\n")

mais_longas = fun.menos_curtas_por_album(dataset_com_ouvintes, dataframe)
print(mais_longas)


#Músicas com menos duração por álbum:
print("\n\n\n\nMúsicas com menos duração por álbum\n\n\n\n")

mais_curtas = fun.mais_curtas_por_album(dataset_com_ouvintes, dataframe)
print(mais_curtas)


# Resposta da pergunta 3

print("\n\n\n\n*****   TOP 5 MÚSICAS MAIS OUVIDAS EM TODA A BANDA    *****")
print("*****   AGUARDE UM MOMENTO, O GRÁFICO SERÁ EXIBIDO POR 6 SEGUNDOs E EM SEGUIDA SALVO NO DIRETÓRIO dataset_etapa_1    *****\n\n\n\n")

mais_ouvida_geral = fun.musica_mais_tocada()


print("\n\n\n\n*****   TOP 5 MÚSICAS MENOS OUVIDAS    *****")
print("*****   AGUARDE UM MOMENTO, O GRÁFICO SERÁ EXIBIDO POR 6 SEGUNDOS E EM SEGUIDA SALVO NO DIRETÓRIO dataset_etapa_1    *****\n\n\n\n")

menos_ouvida_geral = fun.musica_menos_tocada()



# Resposta da pergunta 4
print("\n\n\n\nTOP 5 com menor duração de todas as músicas\n\n\n\n")

dataframe_duracao = dataset_com_ouvintes.rename(columns={"Duracao(seg)":"Duracao"})
dataframe_duracao_maior = dataframe_duracao.copy()
dataframe_duracao_maior = dataframe_duracao_maior[dataframe_duracao_maior.Duracao != "Nan"]
dataframe_duracao_maior = dataframe_duracao_maior.reset_index().drop("Album", axis=1)
dataframe_duracao_maior['Duracao'] = dataframe_duracao_maior['Duracao'].astype(float)
dataframe_duracao_maior = dataframe_duracao_maior.drop_duplicates().sort_values(by="Duracao", ascending=True)[:5]
dataframe_duracao_maior.drop(["Letra", "Popularidade","Ouvintes"], axis=1, inplace=True)

print(dataframe_duracao_maior)
import matplotlib.pyplot as plt
grafico_menor_duracao = dataframe_duracao_maior.plot(x="Musica", y="Duracao", kind="bar")
grafico_menor_duracao.plot()
plt.savefig("menor_duracao_geral")
plt.show(block=False)
plt.pause(6)
plt.close()



print("\n\n\n\nTOP 5 com maior duração de todas as músicas\n\n\n\n")
print("*****   AGUARDE UM MOMENTO, O GRÁFICO SERÁ EXIBIDO POR 6 SEGUNDOS E EM SEGUIDA SALVO NO DIRETÓRIO dataset_etapa_1    *****\n\n\n\n")

dataframe_duracao = dataset_com_ouvintes.rename(columns={"Duracao(seg)":"Duracao"})
dataframe_duracao_maior = dataframe_duracao.copy()
dataframe_duracao_maior = dataframe_duracao_maior[dataframe_duracao_maior.Duracao != "Nan"]
dataframe_duracao_maior = dataframe_duracao_maior.reset_index().drop("Album", axis=1)
dataframe_duracao_maior['Duracao'] = dataframe_duracao_maior['Duracao'].astype(float)
dataframe_duracao_maior = dataframe_duracao_maior.drop_duplicates().sort_values(by="Duracao", ascending=False)[:6]
dataframe_duracao_maior.drop(235, axis=0, inplace=True)
dataframe_duracao_maior.drop(["Letra", "Popularidade","Ouvintes"], axis=1, inplace=True)


print(dataframe_duracao_maior)
grafico_menor_duracao = dataframe_duracao_maior.plot(x="Musica", y="Duracao", kind="bar")
grafico_menor_duracao.plot()
plt.savefig("maior_duracao_geral")
plt.show(block=False)
plt.pause(6)
plt.close()



#Pergunta 5

premios = premios_album()
print(premios)




# Pergunta 6
# Gráfico de Dispersão da relação de duração das músicas com a quantidade de vezes ouvida
print("\n\n\n\n Gráfico de Dispersão da relação de duração das músicas com a quantidade de vezes ouvida\n\n\n\n")

df = dataframe_duracao.copy()
df = df.reset_index()
df.drop(["Letra","Album", "Musica"], axis=1, inplace=True)
df = df.astype(float)
sns.scatterplot(data=df, x="Duracao", y="Ouvintes")
plt.xlim([0,550])
plt.show(block=False)
plt.pause(6)
plt.close()
plt.savefig("relacao_duracao_ouvintes")
