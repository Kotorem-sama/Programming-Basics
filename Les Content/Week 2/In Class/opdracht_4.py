# 4. Gegeven een string en een lijstschrijf
s = "team"
l = [1, "Vreugde", 54, "team", 15]

# Schrijf een programma dat:
# a) als string s een element van de lijst is,
# wordt de index van het element afgedrukt,
# anders wordt "item niet gevonden" afgedrukt
if s in l:
    print(l.index(s))
else:
    print("item niet gevonden")

# b) converteert de lijst naar een string en drukt het af
print("".join(map(str,l)))