#!/usr/bin/python3
import sys
args = sys.argv[1:]
totallines = 0
totalwords = 0
totalchars = 0
for arg in args:
    fd = open('test.py')
    content = fd.read()
    numwords = len(content.split())
    numchars = len(content)
    numlines = len(content.split('\n'))
    totallines += numlines
    print(f'{numlines:>6}{numwords:>6}{numchars:>6} {arg}')
    print(f'{totallines:>6}{totalwords:>6}{totalchars:>6} total')
