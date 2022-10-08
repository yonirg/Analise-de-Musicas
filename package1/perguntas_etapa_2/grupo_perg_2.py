
import funcoes as fun
from dataframes_prontos import df_unicas
import matplotlib.pyplot as plt
#Resposta da perguna 1


texto_albuns, palavras_mais_comuns_albuns = fun.albuns_mais_plv()

print(f"\n\n\n\nNúmero de vezes que cada palavra aparece nos álbuns:\n\n{palavras_mais_comuns_albuns}")

print("\n\n\n\nWordCloud das palavras mais comuns nos nomes dos álbuns\n\n")
nuvem_palavras_comuns_album = fun.wordcloud_album(texto_albuns)
#print(nuvem_palavras_comuns_album)


#Resposta da perguna 2

texto_musicas, palavras_mais_comuns_nomes_musicas = fun.musicas_mais_plv()

print(f"\n\n\n\nNúmero de vezes que cada palavra aparece nos nomes das músicas:\n\n{palavras_mais_comuns_nomes_musicas}")
print("\n\n\n\nWordCloud das palavras mais comuns nos nomes das músicas\n\n")
nuvem_palavras_comuns_nomes_musicas = fun.wordcloud_musica(texto_musicas)


#Resposta da perguna 3
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  REVER   @@@@@@@@@@@@@@@@@@@@@@@@@
fun.letras_por_album()



#Resposta da perguna 4
print("\n\n\n\nWordCloud das palavras mais comuns nas letras das músicas(Aguarde, a imagem será aberta)\n\n\n\n")
df_letras, contagem_palavras = fun.letras_mais_plv()
fun.letras_wordcloud(df_letras)
print(f"Número de vezes que cada palavra aparece nas letras das músicas:\n\n{contagem_palavras}")





#Resposta da perguna 5




#Resposta da pergunta 6
# Se o nome da música a aparecer na letra a coluna recorrencia_nome_musica terá valor True
print("\n\n\n\nRecorrência do nome da música na letra\n\n\n\n")
df_recorrencia_nome_musica = fun.recorrencia_nome_musica(df_unicas)
print("\n\n\n\n")
print(df_recorrencia_nome_musica["recorrencia_nome_musica"].value_counts())
label = ["Nome da música recorrente na letra", "Nome da música não recorrente na letra"]
pizza_recor_musica = plt.pie(df_recorrencia_nome_musica["recorrencia_nome_musica"].value_counts(), labels=label)
plt.savefig("recorrencia_nomes_musicas_letras")
plt.show(block=False)
plt.pause(6)
plt.close()