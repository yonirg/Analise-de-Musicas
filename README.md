<h1>Análise de músicas da banda Imagine Dragons</h1>
> Status: Concluído

<h3>Índice:</h3>
=================

   * [Sobre o projeto](#sobre)
   * [Como ler esse projeto?](#como-ler)
   * [Respostas](#respostas)
   * [Nossa Equipe](#equipe)



<h3 id=sobre>Sobre o projeto:</h3>

Este projeto tem como objetivo fazer uma análise das músicas e dos álbuns do Imagine Dragons.
Para realizá-lo utilizamos dados do site Last.fm (https://www.last.fm/pt/home) para buscar as informações sobre os albuns, as músicas e os ouvintes.
Para buscar as letras das músicas, utiliamos o site letras (https://www.letras.mus.br/).
E, para buscar informações como duração da música e popularidade, utilizamos a biblioteca spotipy, que é conectada a API do Spotify.


<h3 id=como-ler>Como ler esse projeto?</h3>
Para entender e executar esse projeto siga as seguintes instruções:
  
- [ ] Instale em seu computador a biblioteca BeautifulSoup do Python
  
```
pip install beautifulsoup4
```

- [ ] Instale em seu computador a biblioteca urllib3
  
```
pip install urllib3
``` 
- [ ] Instale a biblioteca requests do Python
  
```
pip install requests
```
  
- [ ] Instale a biblioteca matplotlib do Python
  
```
pip install matplotlib
```
  
- [ ] Instale a biblioteca seaborn do Python
  
```
pip install seaborn
```

- [ ] Instale a biblioteca pandas do Python
  
```
pip install pandas
```

- [ ] Instale a biblioteca sys do Python
  
```
pip install sys
```


- [ ] Instale a biblioteca Wordcloud do Python
  
```
pip install wordcloud
```

- [ ] Instale a biblioteca re do Python
  
```
pip install re
```

- [ ] Instale a biblioteca spotipy do Python
  
```
pip install spotipy
```

<strong>OBSERVAÇÃO</strong>:

<strong>Para aumentar a eficiência do projeto, ou seja, torná-lo mais rápido no geral, e principalmente, na visualização das respostas às perguntas, optamos por
converter os dataframes necessários no formato .csv. E, assim, utilizarmos eles já prontos, sem a necessidade de sempre gerá-los novamente.</strong>


- [ ] Instale o arquivo .zip do projeto completo aqui no GitHub
- [ ] Abra o projeto no editor de código de sua preferência
- ETAPA 1:
- [ ] Para visualizar o dataset do projeto acesse o diretório package1, acesse a pasta dataset_etapa_1 e execute o arquvio dataset_final.py 
- ETAPA 2:
- [ ] No diretório package1, acesse a pasta perguntas_etapa_2 e execute o arquvio grupo_perg_1.py epara ver as respostas do grupo 1 de perguntas
- [ ] No diretório package1, acesse a pasta perguntas_etapa_2 e execute o arquivo grupo_perg_2.py para ver as respostas do grupo 2 de perguntas
- [ ] No diretório package1, acesse a pasta perguntas_etapa_2 e execute o arquivo grupo_perg_3.py para ver as respostas do grupo 3 de perguntas

- [ ] Dataset:
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/dataset.PNG)


  <h3 id=respostas>Respostas:</h3>
  Obs: Para exibir alguns dataframes aqui, apenas para fins de estética, a função display do Notebook Jupyter foi utilizada.

  A realização dos passos acima gerará as seguintes repostas às perguntas propostas no trabalaho:
  
  GRUPO DE PERGUNTAS 1:
  
  1) a) Mais Ouvidas por álbum
  
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp1/1a.PNG)
  
  
  
  b) Menos Ouvidas por álbum
  
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp1/1b.PNG)
  
  
  2) a) Mais Longas por álbum
  
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp1/2a.PNG)
  
  
  
  b) Mais Curtas por álbum
  
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp1/2b.PNG)
  
  
  3) a) Menos ouvidas em toda hisória
  
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp1/3a.png)
  
  
  
  b) Mais ouvidas em toda história
  
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp1/3b.PNG)
  
  
  
  4) a) Mais longas em toda história
   
   
   ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp1/4b.PNG)

  
  b) Mais curtas em toda história
  
  
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp1/4a.PNG)

  
  5)  Prêmios por Álbum
  
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp1/5.PNG)

  
  
  6) Relação Duração e quantidade de ouvintes
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp1/6.png)
  
  GRUPO DE PERGUNTAS 2:
  
  1)Mais comuns nos títulos dos álbuns
  
  
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp2/1.PNG)
  
  2) Mais comuns nos títulos das músicas



  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp2/2.png)
  

  
  
  4) Mais comuns nas letras das músicas em toda discografia
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp2/4.png)

  
  
  5) Título de álbum não é um tema tão recorrente nas letras
  
  
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp2/5.png)
  
  
  6) Título de músicas são temas recorrente nas letras
  
  
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp2/6.png)
  
  GRUPO DE PERGUNTAS 3:
  
  1)QUANTAS NOMEAÇÕES A BANDA TEVE?
  
  
  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp3/1.PNG)

  
  2)QUAIS FORAM OS ANOS QUE A BANDA MAIS GANHOU PRÊMIO?



  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp3/2.PNG)

  
  3)QUAIS PREMIOS A BANDA GANHOU EM TODA SUA DISCOGRAFIA?



  ![alt text](https://github.com/yonirg/Analise-de-Musicas/blob/unida/imgs/grp3/3.PNG)


  <h3 id=equipe>Nossa equipe:</h3>
  
  
  * [Lucas Hwang Cuan](https://github.com/Lhc128)

  * [Yonathan Rabinovici Gherman](https://github.com/yonirg)
   
