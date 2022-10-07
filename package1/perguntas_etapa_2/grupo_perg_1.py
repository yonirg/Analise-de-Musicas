import funcoes as fun
import pandas as pd

from dataframes_prontos import dataframe, dataset_com_ouvintes
# Resposta da pergunta 1

#Músicas com mais ouvintes por álbum:
mais_ouvintes = fun.mais_ouvintes_por_album(dataset_com_ouvintes, dataframe)
print(mais_ouvintes)

#Músicas com menos ouvintes por álbum:

menos_ouvintes = fun.menos_ouvintes_por_album(dataset_com_ouvintes, dataframe)
print(menos_ouvintes)






# Resposta da pergunta 2

#Músicas com mais duração por álbum:

mais_longas = fun.menos_curtas_por_album(dataset_com_ouvintes, dataframe)
print(mais_longas)


#Músicas com menos duração por álbum:

mais_curtas = fun.mais_curtas_por_album(dataset_com_ouvintes, dataframe)
print(mais_curtas)


# Resposta da pergunta 3

print("*****   TOP 5 MÚSICAS MAIS OUVIDAS    *****\n\n")
mais_ouvida_geral = fun.musica_mais_tocada()


print("*****   TOP 5 MÚSICAS MENOS OUVIDAS    *****\n\n")
menos_ouvida_geral = fun.musica_menos_tocada()



# Resposta da pergunta 4
dataframe_duracao = dataset_com_ouvintes.rename(columns={"Duracao(seg)":"Duracao"})
dataframe_duracao = dataframe_duracao[dataframe_duracao.Duracao != "Nan"]
dataframe_duracao_menor = dataframe_duracao['Duracao'].astype(int).sort_values(ascending=True)[:7]
dataframe_duracao_menor = pd.DataFrame(dataframe_duracao_menor).reset_index().drop("Album", axis=1).drop_duplicates()
print("TOP 5 com menor duração de todas as músicas\n\n")
print(dataframe_duracao_menor)
print("TOP 5 com maior duração de todas as músicas\n\n")
dataframe_duracao_maior = dataframe_duracao['Duracao'].astype(int).sort_values(ascending=False)[:11]
dataframe_duracao_maior = pd.DataFrame(dataframe_duracao_maior).reset_index().drop("Album", axis=1).drop_duplicates()
print(dataframe_duracao_maior)
