#!/usr/bin/python3
import gspread
import subprocess

dmesg_output = subprocess.run(['dmesg'], capture_output=True, text=True).stdout

dmesg_sec = subprocess.run(['awk', '-F[][]', '{print $2}'], input=dmesg_output, capture_output=True, text=True).stdout

print(dmesg_sec)
