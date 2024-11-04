# 6. Schrijft een programma dat twee getallen accepteert als input van de gebruiker en:
# a) drukt een foutmelding af als het tweede getal kleiner is dan nul.
# b) berekent het eerste getal tot de macht van het tweede getal als het tweede getal tussen 0 en minder dan 4 ligt.
# c) berekent het product van de twee getallen als het tweede getal tussen 4 en minder dan 6 ligt.
# d) berekent de som van de twee getallen als het tweede getal tussen 6 en 10 ligt (inbegrepen)
# e) Als het tweede getal groter is dan 10, wordt er een bericht afgedrukt dat de invoer niet geldig is
# f) gebruik try - except om de verkeerde invoer van de gebruiker op te vangen.

i1 = input("Getal 1: ")
try:
    i1 = int(i1)
except:
    print("Invoer niet geldig")
    exit()

i2 = input("Getal 2: ")
try:
    i2 = int(i2)
except:
    print("Invoer niet geldig")
    exit()

if i2 > 0:
    if i2 < 4:
        print(i1**i2)
    elif i2 < 6:
        print(i1*i2)
    elif i2 <= 10:
        print(i1+i2)
    else:
        print("Invoer niet geldig")
else:
    print("Invoer niet geldig")