# 16. Bereken (met while of for) het gemiddelde van de volgende cijferlijst:
# cijferlijst = [9.8, 7.6, 7.1, 8.7, 8.3, 9.0, 5.7, 7.9, 8.2, 9.4]

cijferlijst = [9.8, 7.6, 7.1, 8.7, 8.3, 9.0, 5.7, 7.9, 8.2, 9.4]

totaal = 0.0
aantal = len(cijferlijst)

while cijferlijst:
    totaal += cijferlijst.pop()

print(f"Het gemiddelde is: {totaal//aantal}")