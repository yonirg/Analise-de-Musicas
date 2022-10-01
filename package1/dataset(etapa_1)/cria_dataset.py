import modulo_dataset as mds

dict_albuns_musicas = mds.albuns_musicas()

arrays = mds.auxiliar_multi_index(dict_albuns_musicas)

dataframe = mds.df_MI(arrays)

df_unicas = mds.pega_letras_unicas(dataframe)

dataframe_com_letras = mds.letras_df(dataframe, df_unicas)


