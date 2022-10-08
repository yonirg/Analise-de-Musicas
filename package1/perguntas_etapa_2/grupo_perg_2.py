
import funcoes as fun

#Resposta da perguna 1
"""

texto_albuns, palavras_mais_comuns_albuns = fun.albuns_mais_plv()

print(f"\n\n\n\nNúmero de vezes que cada palavra aparece nos álbuns:\n\n{palavras_mais_comuns_albuns}")

print("\n\n\n\nWordCloud das palavras mais comuns nos nomes dos álbuns\n\n")
nuvem_palavras_comuns_album = fun.wordcloud_album(texto_albuns)
#print(nuvem_palavras_comuns_album)


#Resposta da perguna 2
"""
texto_musicas, palavras_mais_comuns_nomes_musicas = fun.musicas_mais_plv()

print(f"\n\n\n\nNúmero de vezes que cada palavra aparece nos nomes das músicas:\n\n{palavras_mais_comuns_nomes_musicas}")
print("\n\n\n\nWordCloud das palavras mais comuns nos nomes das músicas\n\n")
nuvem_palavras_comuns_nomes_musicas = fun.wordcloud_musica(texto_musicas)


#Resposta da perguna 3
fun.letras_por_album()


"""
#Resposta da perguna 4
print("\n\n\n\nWordCloud das palavras mais comuns nas letras das músicas(Aguarde, a imagem será aberta)\n\n\n\n")
df_letras, contagem_palavras = fun.letras_mais_plv()
fun.letras_wordcloud(df_letras)
print(f"Número de vezes que cada palavra aparece nas letras das músicas:\n\n{contagem_palavras}")





#Resposta da perguna 5


"""
