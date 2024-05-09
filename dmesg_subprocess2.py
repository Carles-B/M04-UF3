#!/usr/bin/python3
import gspread
import subprocess
import time
import datetime

gc = gspread.service_account(filename='/home/enti/.config/gspread/service_account.json')
sht = gc.open("dmesg")

fecha = datetime.datetime.now().strftime("%Y-%m-%d")

dmesg = subprocess.getoutput("dmesg")

dmesg_data = []

dmesg_lines = dmesg.splitlines()

for dmesg_line in dmesg_lines:
	dmesg_temp = dmesg_line.split("[")[1]
	
	dmesg_time = dmesg_temp.split("]")[0]
	
	dmesg_temp = dmesg_temp.split("]")[1]
	
	dmesg_temp = dmesg_temp.split(":")

	dmesg_module = dmesg_temp[0]

	dmesg_info = ""

	if len(dmesg_temp) > 1:
		dmesg_info = dmesg_temp[1]
	
	dmesg_data.append([dmesg_time, dmesg_module, dmesg_info])


wks_list = sht.worksheets()
exist = False

for wks in wks_list:
	if fecha == wks.title:
		exist = True
		sht.worksheet(fecha).clear()

if not exist:
	sht.add_worksheet(fecha, 3, 3, index=None)
	
sht.worksheet(fecha).append_rows(dmesg_data)

