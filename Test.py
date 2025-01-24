import requests
import json
import pandas as pd


def get_info(df):
    info = []
    for x in range(0,len(df)-1):
        info.append(df[x]['info'])
    return info
#idea
#Obtener base de datos de nombres de genderize, separar los nombres deseados hasta obtener
#el porcentaje de confianza deseado. Luego, crear un ciclo for que itere sobre los elementos del arreglo
#armar un link concatenando la información a q
#Armar un df y finalmente concatenar los DF
response = requests.get("https://dblp.org/search/publ/api?q=Ana$&format=json")

dictr = response.json()
hits =  dictr['result']['hits']['hit']

info = get_info(hits)


# df = pd.json_normalize(recs)
# print(df.columns)
# print(df)
# recs = 
# print(df.columns)
print(pd.json_normalize(hits).columns)
# for i in info:
#     print(pd.json_normalize(i))
