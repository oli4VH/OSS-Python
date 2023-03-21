#!/usr/bin/python3
import sys

# Haal het patroon op uit de eerste parameter
pattern = sys.argv[1]

# Loop door de bestanden die als parameters zijn meegegeven
for file_path in sys.argv[2:]:
    # Open het bestand
    with open(file_path, 'r') as file:
        # Loop door de regels in het bestand
        for line in file:
            # Zoek naar het patroon in de regel
            if pattern in line:
                # Als het patroon in de regel voorkomt, print dan de regel
                print(line.strip())
