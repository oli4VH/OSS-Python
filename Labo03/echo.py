#!/usr/bin/python3
import sys

# alle command line argumenten, behalve de naam van het script
for arg in sys.argv[1:]:
    # Print het argument met een spatie als scheidingsteken
    print(arg, end=' ')
# Print een lege lijn
print()
