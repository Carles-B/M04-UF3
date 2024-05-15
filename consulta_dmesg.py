#!/usr/bin/python3

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
import pkg_resources

import gspread
import csv
import gzip
import re


def upload_file_to_gdrive():
	credentials_path = '/home/enti/.config/gspread/service_account.json'
	scope = 'https://www.googleapis.com/auth/drive'
	gauth = GoogleAuth()

	gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(
		credentials_path, scope)
	
	drive = GoogleDrive(gauth)

	folder_name = "dmesg gz"
	parent_directory_id = "1l0SYMw-5k8l42wvioK2p3XXPPGItGQH5"

	folder_metadata = {
		'title': folder_name,
		'mimeType': 'application/vnd.google-apps.folder',
		'parents': [{'id': parent_directory_id}]
	}
	
	folder_id = None
	foldered_list = drive.ListFile(
		{'q': "'"+parent_directory_id+"' in parents and trashed=false"}).GetList()
	
	for file in foldered_list:
		if (file['title'] == folder_name):
			folder_id = file['id']
	
	if folder_id == None:
		folder = drive.CreateFile(folder_metadata)
		folder.Upload()
		folder_id = folder.get("id")
	
	return drive, folder_id

def main():
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
						buscar = input("\nIntroduce una palabra clave para la busqueda: ")
						resultados_busqueda = []

						for registro in valores:
							for campo in registro:
								if re.search(buscar, campo, re.IGNORECASE):
									resultados_busqueda.append(registro)

						if resultados_busqueda:
							print("\nResultados de la búsqueda:")
							for resultado in resultados_busqueda:
								print(resultado)
								print("\n")
						else:
							print("No se encontraron coincidencias \n")

						#Declaro la variable con el nombre.csv
						filename = f"{seleccion}.csv"

						#Abro el archivo y escribo ("w") los registros en el formato correcto
						with open(filename, "w", newline="") as file_csv:
							file_csv.write(registros_formateados)
						print(f"los archivos se han guardado en {filename}")

						#Hago gzip del archivo.csv
						gzip_filename = f"{filename}.gz"
						with open(filename, "rb") as f_in:
							with gzip.open(f"{filename}.gz", "wb") as f_out:
								f_out.writelines(f_in)
								print(f"El gzip del csv se ha guardado correctamente con nombre: {filename}.gz")

						drive, folder_id = upload_file_to_gdrive()
						file_metadata = {
							'parents': [{'id': folder_id}],
							'title': gzip_filename
						}
						file1 = drive.CreateFile(file_metadata)
						file1.SetContentFile(gzip_filename)
						file1.Upload()
						print("\n------------- File is Uploaded -------------")

				except ValueError:
					print("Por fabor, introduce un NÚMERO y que sea válido (entre 1 y 5).")
if __name__ == "__main__":
	main()
