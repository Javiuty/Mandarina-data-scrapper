import pandas as pd

def get_clasifications():
  entries = []

  equipos = ['La Mandarina Mecánica', 'Clara Del Rey', 'La Fuente del Berro FC', 'CD Inter Hispano', 'Carpe diem', 'Fafa juniors', 'Borriquitos', 'Esgolazo FC', 'Berrathinakos', 'Atlético Birgueiro', 'Ajarrax FC', '23' ]

  df = pd.read_csv('clasificaciones.csv', delimiter=';', encoding='latin-1')
  df = df.dropna(how='all')

  for equipo in equipos:
    team = df[df['Nombre_equipo'].str.contains(equipo, na=False)]
    entries.append(team)

  combined_df = pd.concat(entries)

  combined_df.to_json('clasificaciones.json', orient='records', force_ascii=False)

  print('Archivo JSON de las clasificaciones ha sido creado!')