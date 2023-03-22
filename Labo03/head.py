#!/usr/bin/python3
import sys

# Aantal lijnen om te printen
n = 10

# alle command line argumenten, behalve de naam van het script
for arg in sys.argv[1:]:
    # Open het bestand in read-only mode
    with open(arg, 'r') as f:
        # de eerste n lijnen van het bestand
        for i in range(n):
            line = f.readline()
            # Print de lijn als deze niet leeg is
            if line:
                print(line, end='')
    # Sluit het bestand
    f.close()
