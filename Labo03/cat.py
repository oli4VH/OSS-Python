#!/usr/bin/python3
import sys

# alle command line argumenten, behalve de naam van het script
for arg in sys.argv[1:]:
    # Open het bestand in read-only mode
    with open(arg, 'r') as f:
        # Print de inhoud van het bestand
        print(f.read())
    # Sluit het bestand
    f.close()
