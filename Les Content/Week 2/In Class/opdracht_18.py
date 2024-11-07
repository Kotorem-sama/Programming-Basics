# 18. Schrijf een Python-programma waarin:
# a. Een functie wordt gedefinieerd die een lijst van 10 willekeurige gehele getallen tussen 0 en 20 genereert.
# b. Een andere functie wordt gedefinieerd die telt hoe vaak elk getal voorkomt in de gegenereerde lijst.
# c. Het programma de lijst van willekeurige getallen genereert, afdrukt, en vervolgens de frequentie van elk getal in die lijst weergeeft.

# Voorbeeld: 
# Gegenereerde lijst van willekeurige getallen: [4, 12, 15, 4, 19, 12, 0, 7, 4, 3]

# Frequentie van elk getal:
# Getal 4 komt 3 keer voor.
# Getal 12 komt 2 keer voor.
# Getal 15 komt 1 keer voor.
# Getal 19 komt 1 keer voor.
# Getal 0 komt 1 keer voor.
# Getal 7 komt 1 keer voor.
# Getal 3 komt 1 keer voor.

import random

def randomisedList():
    return [random.randint(0, 20) for i in range(0, 10)]

def numberCount(l):
    dictionary = dict.fromkeys(set(l), 0)
    for i in l:
        dictionary[i] += 1
    return dictionary

for key, value in numberCount(randomisedList()).items():
    print(f"Getal {key} komt {value} keer voor.")