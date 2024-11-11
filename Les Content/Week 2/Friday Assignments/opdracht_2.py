# Opdracht 2 Omkeren van getallen
# Pas het rekenmachineproject aan zodat de volgorde van de
# getallen niet uitmaakt. Er zijn een paar manieren om
# hetzelfde resultaat te bereiken; een manier is om de
# gebruiker te vragen of ze de plaatsing van de getallen
# willen omkeren.

possibilities = {
    'multiplication' : '*',
    'devision' : '/',
    'the power of' : '**',
    'addition' : '+',
    'subtraction' : '-',
    'square root': 'sqrt'
}

berekeningen = { '*': lambda x, y: x * y,
                '/': lambda x, y: x / y,
                '**': lambda x, y: x ** y,
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                'sqrt' : lambda x, y: x **(1/y)
                }

print(f"SOORT:\tIN TE VULLEN:".expandtabs(20))
for key, value in possibilities.items():
    print(f"{key}\t{value}".expandtabs(20))

berekening = input("Welke berekening wil je uitvoeren?: ")
if berekening not in possibilities.values():
    print("Vul een van de karakters in de 2e rij in.")
else:
    try:
        nummer_1 = int(input("Wat is het eerste cijfer? "))
        nummer_2 = int(input("Wat is het tweede cijfer? "))
    except:
        print("Vul alsjeblieft een nummer in.")
    else:
        uitkomst = f"{nummer_1}{berekening}{nummer_2}"
        print(f"Dit zal nu worden uitgevoerd: {uitkomst}")
        if input("Wilt u de nummers omdraaien? (y/n) ") == 'y':
            nummer_3 = nummer_1
            nummer_1 = nummer_2
            nummer_2 = nummer_3
        try:
            resultaat = berekeningen[berekening](nummer_1, nummer_2)
            uitkomst = f"{nummer_1}{berekening}{nummer_2}"
            print(f"Het resultaat van {uitkomst} is {resultaat}")
        except ZeroDivisionError:
            print("Kan niet delen door 0.")