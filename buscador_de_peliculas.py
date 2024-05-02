#!/usr/bin/python3
import requests
from colorama import init, Fore

init(autoreset=True)

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

    print(Fore.GREEN + "Título:" + Fore.CYAN + f"{title}")
    print(Fore.GREEN + "Año:" + Fore.CYAN + f"{year}")
    print(Fore.GREEN + "Actores:" +Fore.CYAN + f"{actors}")

