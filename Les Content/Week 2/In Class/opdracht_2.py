# 2. Maak een Python-programma voor een eenvoudig
# beoordelingssysteem. Het programma moet de numerieke
# score van een student (0-100) als invoer nemen en het
# bijbehorende lettercijfer uitprinten volgens
# de volgende regels:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D

try:
    invoer = int(input("Welk cijfer geef je deze student?: "))
    if invoer > 100:
        print("Dit cijfer is hoger dan 100")
    elif invoer >= 90:
        print("A")
    elif invoer >= 80:
        print("B")
    elif invoer >= 70:
        print("C")
    elif invoer >= 60:
        print("D")
    else:
        print("Voor dit programma is alleen gespecificeerd om vanaf 60 te beginnen.")
except:
    print("Deze invoer is geen cijfer")