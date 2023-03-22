#!/usr/bin/python3
import os

# Krijg een lijst van alle bestanden in de huidige map
files = os.listdir()

while True:
    # Vraag de gebruiker om een bestandsnaam
    filename = input("Voer een bestandsnaam in: ")

    # Stop het script als de gebruiker niets invoert
    if filename == "":
        break

    # Controleer of het bestand bestaat
    if filename in files:
        # Als het bestand bestaat, open het en print de inhoud
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    else:
        # Als het bestand niet bestaat, vraag de gebruiker om een tekst en schrijf deze naar het bestand
        text = input("Bestand bestaat niet. Voer tekst in om op te slaan: ")
        with open(filename, 'w') as file:
            file.write(text)
            print("Bestand is aangemaakt en de tekst is opgeslagen.")
