#!/usr/bin/python3
def uniqletters(string, count=1, ignore_case=False):
    if ignore_case:
        string = string.lower()
    resultaat = ''
    for letter in string:
        if resultaat.count(letter) < count:
            resultaat += letter
    return resultaat
