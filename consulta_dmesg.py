#!/usr/bin/python3
import gspread
import csv
import gzip
import re

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
		try:
				numero = int(escoger) - 1 
				seleccion = lista_formateada[numero]
				valores = sht.worksheet(seleccion).get_values()
				print("\nRegistros en la hoja:", seleccion)
				
				registros_formateados = ""

				#Por cada linea (registro) junta los elementos de este separandolos por ;
				for registro in valores:
					registros_formateados += ";".join(registro) + "\n"
				print(registros_formateados)
	
				#busqueda basada en expresiones regulares

				

				#Declaro la variable con el nombre.csv
				filename = f"{seleccion}.csv"

				#Abro el archivo y escribo ("w") los registros en el formato correcto
				with open(filename, "w", newline="") as file_csv:
					file_csv.write(registros_formateados)
				print(f"los archivos se han guardado en {filename}")

				#Hago gzip del archivo.csv
				with open(filename, "rb") as f_in:
					with gzip.open(f"{filename}.gz", "wb") as f_out:
						f_out.writelines(f_in)
						print(f"El gzip del csv se ha guardado correctamente con nombre: {filename}.gz")

		except ValueError:
			print("Por fabor, introduce un NÚMERO y que sea válido (entre 1 y 5).")


