import os
os.system("figlet                     NETT")
print("Repository:        https://github.com/Fandi63/NETT")
print("Options:")
print("                      [1] Test the wifi card")
print("                      [2] Ping google")
print("                      [3] Ping microsoft")
input("nett>")
if input() is 1:
  os.system ("airmon-ng start wlan0")
if input() is 2:
  os.system("ping www.google.com")
if input() is 3:
  os.system("ping www.microsoft.com")
  
