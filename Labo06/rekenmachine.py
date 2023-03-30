#!/usr/bin/python3
while True:
    try:
        num1 = float(input("Voer het eerste getal in: "))
        num2 = float(input("Voer het tweede getal in: "))
        operator = input("Voer een operator in (+, -, *, /): ")
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Fout: delen door nul is niet toegestaan")
                continue
            result = num1 / num2
        else:
            print("Fout: ongeldige operator")
            continue
        
        print("Resultaat: ", result)
        break
        
    except ValueError:
        print("Fout: voer geldige getallen in")
    except KeyboardInterrupt:
        print("Programma afgebroken door gebruiker")
        break
