# 17. Maak een programma waarin je een getal invoert en vervolgens de som
# berekent van dat getal en de volgende 5 opeenvolgende getallen. Gebruik een
# loop om steeds het volgende getal bij de som op te tellen. Wanneer de som is
# berekend, geef het resultaat weer.
# Voorbeeld: input getal = 2 dan is de som: 2 + (3+4+5+6+7) = 27. 3,4,5,6,7
# zijn de 5 opeenvolgende getalen van 2.

nummer = int(input("Geef een nummer: "))
som = 0

for i in range (0, 6):
    som += nummer + i

print(som)