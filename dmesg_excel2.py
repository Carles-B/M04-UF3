#!/usr/bin/python3
import gspread
import sh

dmesg_sec = sh.awk('-F\'[][]\'', '{print $2}', _in=sh.dmesg())
print(dmesg_sec)

dmesg | awk -F'[:]' '{print $1}' | cut -d "]" -f2
