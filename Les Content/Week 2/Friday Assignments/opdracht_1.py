# Opdracht 1 Creating a calculator
# Met de lessen die we deze week hebben geleerd, gaan we een
# eenvoudige rekenmachine bouwen die gebruikersinvoer
# accepteert en het juiste resultaat weergeeft.
# Final design
# •	Vraag de gebruiker naar de berekening die ze willen
#   uitvoeren.
# •	Vraag de gebruiker naar de getallen waarop ze de bewerking
#   willen uitvoeren.
# •	Het programma moet dan:
#     o	De ingevoerde getallen om naar floats.
#     o	De bewerking uitvoeren en het resultaat printen. 
#     o	Als er een uitzondering optreedt, print dan een
#       foutmelding (zoek uit hoe je dat kan doen).


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
        try:
            print(f"Het resultaat is {berekeningen[berekening](nummer_1, nummer_2)}")
        except ZeroDivisionError:
            print("Kan niet delen door 0.")