#!/usr/bin/python3

import requests
import gspread

gc = gspread.service_account()
wks = gc.open("Pelis").sheet1

print("¡Esto es un buscador que guarda en un google sheet!")
name = input("\nIntroduce una película: ")
#url = "https://seearch.imdbot.worksers.dev/?q="+name

#movie = requests.get(url)
#data = movie.json()

#if not data['description']:
#	print("Error: No se han encontrado resultados.")
#else:
#	title = data['description'][0]['#TITLE']
#	year = data['description'][0]['#YEAR']
#	actors = data['description'][0]['#ACTORS']

wks.update_acell('A3', name)
contador = 0

x = wks.col_values(1)
contador += 1
contador += 1
cellA = 'A'+str(contador)
cellB = 'B'+str(contador)
cellC = 'C'+str(contador)
print(cellC)
print(x)
