import modulo_dataset as mds

dict_albuns_musicas = mds.albuns_musicas()

arrays = mds.auxiliar_multi_index(dict_albuns_musicas)

dataframe = mds.df_MI(arrays)

df_unicas = mds.pega_letras_unicas(dataframe)

dataframe_com_letras = mds.letras_df(dataframe, df_unicas)

dataframe_com_duracao = mds.duracao_df(dataframe_com_letras, df_unicas)

dataframe_com_popularidade = mds.popularidade_df(dataframe_com_duracao, df_unicas)

dataset = mds.apagar_colunas(dataframe_com_popularidade,["duration_msright", "Letraright"])
dataset = dataset.rename(columns={"duration_ms":"Duracao(seg)"})
dataset = dataset.rename(columns={"popularity":"Popularidade"})

dataset_com_ouvintes = mds.ouvintes_por_album(dataset)

print(dataset_com_ouvintes)



