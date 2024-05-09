#!/usr/bin/python3
import gspread


gc = gspread.service_account(filename='/home/enti/.config/gspread/service_account.json')
sht = gc.open("dmesg")

wks_list = sht.worksheets()
ultimos5 = wks_list[-5:]
lista_formateada = []

print("¡Esto es un consultor online del registro de dmesg!\n")
print("Esto son los ultimos 5 registros ¿Cual es el que quieres consultar?\n")

for wks in ultimos5:
	print(wks.title)
	lista_formateada.append(wks.title)

salir = False
while not salir: 
	escoger = input("\nIntroduce un numero (si quieres salir escribe 'salir'): ")
	if escoger == 'salir':
		print("Saiendo del programa...")
		salir = True
	else:
		numero = int(escoger) - 1 
		seleccion = lista_formateada[numero]
		valores = sht.worksheet(seleccion).get_values()
		print(valores)

