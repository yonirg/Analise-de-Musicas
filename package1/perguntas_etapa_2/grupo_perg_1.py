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
fun.musicas_menor_duracao()

fun.musicas_maior_duracao()


#Pergunta 5

premios = premios_album()
print(f"\n\n Albuns com mais prêmios: \n{premios}")




# Pergunta 6
# Gráfico de Dispersão da relação de duração das músicas com a quantidade de vezes ouvida
fun.musicas_popularidade_duracao()
