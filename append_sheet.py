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
    wks.append_row([title, year, actors])
