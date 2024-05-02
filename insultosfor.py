#!/usr/bin/python3

import requests

url = "https://evilinsult.com/generate_insult.php?lang=es&type=json"

cataas = requests.get(url)

cat_data = cataas.json()

for fact in cat_data:
	print(fact['insult']+"\n")
