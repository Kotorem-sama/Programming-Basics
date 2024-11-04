#Met https://www.w3schools.com/python/python_ref_string.asp
#Gegeven de volgende string, schrijf een programma dat:
s = "Ik hou van appels, appels zijn mijn favoriete fruit"

# a) het aantal keren dat de letter "a" in de string voorkomt, afdrukt
print(s.count("a"))

# b) waarde 'a' vervangt door 'p' en het resultaat afdrukt
print(s.replace("a", "p"))

# c) de string naar hoofdletters transformeert en het resultaat afdrukt
print(s.upper())

# d) de string naar kleine letters transformeert en het resultaat afdrukt
print(s.lower())

# e) de lengte van de string afdrukt
print(len(s))

# f) elke twee tekens in de string afdrukt (met behulp van slicing)
print(s[::2])

# g) de string omgekeerd afdrukt (met behulp van slicing)
print(s[::-1])