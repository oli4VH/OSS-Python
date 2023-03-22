#!/usr/bin/python3
# open het bestand in write mode
file = open('greeting.txt', 'w')

# schrijf een groet naar het bestand
file.write("Gegroet!\n")

# sluit het bestand
file.close()
