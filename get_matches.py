import pandas as pd

def get_matches():
  df = pd.read_csv('partidos.csv', delimiter=';', encoding='latin-1')
  
  #Eliminar celdas vacías
  df = df.dropna(how='all')

  equipo_local = 'La Mandarina Mecánica'
  df_filtrado_local = df[df['Equipo_local'].str.contains(equipo_local, na=False)]

  equipo_visitante = 'La Mandarina Mecánica'
  df_filtrado_visitante = df[df['Equipo_visitante'].str.contains(equipo_visitante, na=False)]

  df_filtrado = pd.concat([df_filtrado_local, df_filtrado_visitante])

  df_filtrado = df_filtrado.drop_duplicates()

  df_filtrado = df_filtrado.sort_values(by='Fecha', ascending=False)

  # Filtrado para partidos
  df_filtrado = df_filtrado[['Fecha', 'Hora', 'Equipo_local', 'Equipo_visitante', 'Nombre_competicion', 'Estado', 'Campo', 'Jornada', 'Partido', 'Resultado1', 'Resultado2', 'Color_Camiseta_1', 'Color_Camiseta_2', 'Observaciones', 'SISTEMA_COMPETICION']]

  df_filtrado = df_filtrado.reset_index(drop=True)

  df_filtrado.to_json('partidos.json', orient='records', force_ascii=False)

  print('Archivo JSON de los partidos ha sido creado!')

