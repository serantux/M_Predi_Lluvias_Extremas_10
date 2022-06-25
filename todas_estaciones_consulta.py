# 117bcd7ca3a8e87bb63dff50b177f170
# 9349598e9f11f5eddceb6791daa6d787
# e6af5b5feb891b272e18f5e2fc0370a6


import requests
import pandas as pd
from collections import namedtuple


# Listado de variables que necesito
var = 'time,summary,precipAccumulation,precipIntensity,precipIntensityMax,\
precipProbability,precipType,humidity,pressure,windSpeed,uvIndex,temperatureMin,temperatureMax,omm_esta,codigo'
# Transformo en listado
features = var.split(',')
# print(features) #Control de variables

DailySummary = namedtuple("DailySummary", features)
DailySummary

df1 = pd.DataFrame()
key = '9349598e9f11f5eddceb6791daa6d787'
baseUrl="https://api.darksky.net/forecast"

df1 = pd.DataFrame()
lista_consulta=[]



for i in range(len(filtered_df)):
  
  
  lon_dec=filtered_df.iloc[i]['lon_dec']
  lat_dec=filtered_df.iloc[i].lat_dec
  omm_esta = filtered_df.iloc[i].nombre
  codigo = filtered_df.iloc[i].omm_id

  print(f'\nUrl para la estación: {filtered_df.iloc[i].nombre} - código: {filtered_df.iloc[i].omm_id}')

  for unix in range(1625116548, 1655932860, 86400): 
    consulta = f'{baseUrl}/{key}/{lat_dec},{lon_dec},{unix}?exclude=flags,hourly&units=si'                                   
    try:
      
      r = requests.get(consulta)
      data = r.json()
      df = pd.DataFrame(list(data["daily"]["data"]))
      df['omm_esta'] = omm_esta
      df['codigo'] = codigo
      
      df1 = pd.concat([df1, df])
      lista_consulta.append(data)
    
    except:
      
      print(f'la estacion: {omm_esta} - No posee datos para la fecha en formato unix:{unix}')
      pass
  #   break
  # break
# print(f'resultado de las consultas \n {lista_consulta}')
res = pd.DataFrame(df1, columns=features)
res.reset_index()


res.to_csv('muestra_2021_2022.csv', sep=';',index=False)

# Almacenando en formato CSV:
from google.colab import files
files.download('muestra_2021_2022.csv')


# Almacenando en forma de documento txt las consultas previas
listitems = lista_consulta.copy()
with open('consulta.txt', 'w') as temp_file:
    for item in listitems:
        temp_file.write("%s\n" % item)
file = open('consulta.txt', 'r')
#print(file.read()])
print(listitems[0])


from google.colab import files
files.download('consulta.txt')
