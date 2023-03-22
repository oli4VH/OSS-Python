#!/usr/bin/python
# open het bestand in read mode
file = open('greeting.txt', 'r')

# lees de inhoud van het bestand en sla deze op als een string
content = file.read()

# print de inhoud van het bestand
print(content)

# sluit het bestand
file.close()
