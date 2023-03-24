#!/usr/bin/python3
def maaltafel(getal, maximum=10):
    maalresultaten = []
    for i in range(1, maximum+1):
        maalresultaten.append(getal * i)
    return maalresultaten
