#!/usr/bin/python3
import requests
from colorama import init, Fore
import gspread

gc = gspread.service_account()
wks = gc.open("Pelis").sheet1

print(Fore.YELLOW + "¡Esto es un buscador de películas!")
name = input(Fore.GREEN + "\nIntroduce una película: " + Fore.CYAN)
url = "https://search.imdbot.workers.dev/?q="+name

movie = requests.get(url)
data = movie.json()

if not data['description']:
    print(Fore.RED + "Error: No se han encontrado resultados.")

else:
    title = data['description'][0]['#TITLE']
    year = data['description'][0]['#YEAR']
    actors = data['description'][0]['#ACTORS']
    contador = 0
    for x in wks.col_values(1):
        contador += 1
    contador += 1
    cellA = 'A'+str(contador)
    cellB = 'B'+str(contador)
    cellC = 'C'+str(contador)

    wks.update_acell(cellA, title)
    wks.update_acell(cellB, year)
    wks.update_acell(cellC, actors)

