#!/usr/bin/python3

import requests

url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

insulto = requests.get(url)
i = insulto.json()

print(i['insult'])
