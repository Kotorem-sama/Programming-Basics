# Opdracht 2 Onderzoeksmethoden.
# We hebben een aantal van de veelgebruikte methoden voor
# stringmanipulatie besproken; er zijn er echter nog veel
# meer; probeer er een paar op te zoeken en te implementeren.

# 1) .zfill()
# Vult de string met '0' tot het 10 karakters lang is
s1 = "22"
print(f"{len(s1)}\t'{s1}'")
s1 = s1.zfill(10)
print(f"{len(s1)}\t'{s1}'")

#2) .translate()
# Kan meerdere karakters tegelijk vervangen unlike .replace().
# Je moet in de haakjes een tabel toevoegen. Je creëert de
# tabel met str.maketrans(). Deze tabel koppelt de eerste
# karacter van de eerste parameter aan de eerste karakter
# van de tweede parameter. De derde geeft aan welke karacters je
# van de string wilt verwijderen. Alles is hoofdletter gevoelig.
# De methode verwijdert eerst de gewilde karakters, dan 
# worden de andere karakters vervangen
s1 = "Good night Samy!"
s2 = "mSa"
s3 = "eJo"
s4 = "Oy"
tabel = str.maketrans(s2, s3, s4)
s1.translate(tabel)
print(s1)

#3) .capitalize()
# Verandert de eerste karakter naar grote letter en de rest
# in kleine letters. Als de string begint met een nummer,
# gebeurt hier niets mee.
s1 = "python is DECENTLY fun"
s1 = s1.capitalize()
print(s1)

# 4) .casefold()
# Is een zelfde soort functie als .lower(), maar veel
# agressiever. terwijl lower ~300 karakters kan identifiseren
# en naar kleine letters kan omzetten, kan .casefold() ~150.000
# karakters omzetten.
s1 = "Straße"
s1 = s1.casefold()
print(s1)

# 5) .center()
# Is een methode die de string centreert. Je specificeert de
# lengte van de string die wordt terug gegeven en karakter.
# De standaard is een spatie. Als de lengte van de string
# groter is dan wat je invult zal de string in zijn geheel
# worden terug gekeert.
s1 = "center"
s1 = s1.center(50, "'")
print(s1)

# 6) .count()
# Is een methode die de hoeveelheid van het meegegeven woord
# terug keert. De 2e en 3e parameter zijn de start- en
# eindpositie van de cursor als je alleen een deel van de
# string wilt tellen.
s1 = "I love it when I lay down in the sand, because I like it"
i1 = s1.count("I")
print(i1)

# 7) .encode()
# Is een methode die de string encodeert in een specifieke
# codec. Je kan met de methode de encoding selecteren en
# wat de methode doet als een karakter niet voor komt in de
# encoding (aka errors). De verschillende codecs kan je vinden op:
# https://docs.python.org/3.13/library/codecs.html#standard-encodings
# De error methodes worden hier onder weergegeven.
s1 = "1. This happens: å"
print(s1.encode("ascii","backslashreplace"))
print(s1.encode("ascii","ignore"))
print(s1.encode("ascii","namereplace"))
print(s1.encode("ascii","replace"))
print(s1.encode("ascii","xmlcharrefreplace"))

# 8) .endswith()
# Is een methode die checkt (in een aangegeven range) of de
# string eindigd met een meegegeven string. Keert boolean terug.
s1 = "There are so many methods for strings :("
print(s1.endswith(":(", 8, 23))

# 9) .expandtabs()
# Verandert de lengte van tabs in strings. Standaard is 8
s1 = "H\te\tl\tl\to"
print(s1)
print(s1.expandtabs(16))

# 10) .find()
# Vind de index van de eerste instantie van de meegegeven
# string. Unlike .index() geeft het geen error als het niets
# kan vinden, maar keert het een -1 terug. Je kan met de 2e
# en 3e parameter de start en stop van de positie meegeven.
s1 = "waar zal de x staan?"
print(s1.find("al"))

# Vind meer op https://www.w3schools.com/python/python_ref_string.asp