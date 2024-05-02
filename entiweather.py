#!/usr/bin/python3

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=41.382274191583036&longitude=2.1166885842478287&current=temperature_2m"
temperatura = requests.get(url)

T= temperatura.json()
temp = T['current']['temperature_2m']
units = T['current_units']['temperature_2m']

print(f"La ttemperatura en ENTI es: {temp}{units}")
