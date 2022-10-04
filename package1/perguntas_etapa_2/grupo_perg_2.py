
import funcoes as fun

#Resposta da perguna 1

texto, palavras_mais_comuns = fun.albuns_mais_plv()

print(f"Número de vezes que cada palavra aparece nos álbuns:\n\n{palavras_mais_comuns}")

print("\n\nWordCloud das palavras mais comuns nos nomes dos álbuns\n\n")
nuvem_palavras_comuns_album = fun.wordcloud_album(texto)
print(nuvem_palavras_comuns_album)


#Resposta da perguna 2



#Resposta da perguna 3




#Resposta da perguna 4
print("\n\nWordCloud das palavras mais comuns nas letras das músicas(Aguarde, a imagem será aberta)\n\n")
fun.letras_wordcloud()
palavras_mais_comuns_letra = fun.letras_mais_plv()
print(f"Número de vezes que cada palavra aparece nas letras das músicas:\n\n{palavras_mais_comuns_letra}")





#Resposta da perguna 5


