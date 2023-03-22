#!/usr/bin/python3
import sys

# Begin lijnnummer
line_number = 1

# alle command line argumenten, behalve de naam van het script
for arg in sys.argv[1:]:
    # Open het bestand in read-only mode
    with open(arg, 'r') as f:
        # over elke lijn in het bestand
        for line in f:
            # Print het lijnnummer, geformatteerd als 6-tekens breed getal, gevolgd door een tab en lijnnummer
            print('{:6d}\t{}'.format(line_number, line), end='')
            # Verhoog het lijnnummer
            line_number += 1
    # Sluit het bestand
    f.close()
