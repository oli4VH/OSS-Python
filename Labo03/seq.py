#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description='Print een opeenvolgende reeks getallen.')
parser.add_argument('eind', metavar='EIND', type=int, help='het laatste getal in de reeks')
parser.add_argument('-s', '--separator', metavar='SEPARATOR', type=str, default='\n',
                    help='het scheidingsteken tussen de getallen')
parser.add_argument('-f', '--format', metavar='FORMAT', type=str, default='%g',
                    help='het aangepaste opmaakformaat')
parser.add_argument('-w', '--equal-width', action='store_true',
                    help='vul het uitvoerveld aan tot een vaste breedte met nullen')
args = parser.parse_args()

if args.equal_width:
    width = len(str(args.eind))
    fmt = '%0' + str(width) + 'd' + args.separator
else:
    fmt = args.format + args.separator

for i in range(1, args.eind+1):
    print(fmt % i, end='')
