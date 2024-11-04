# Opdracht 1 Creating a Receipt Printing Program
# Welkom bij je eerste project! We gaan een heel basicprogramma voor het printen van bonnetjes maken.
# Deze week, omdat we over variabelen, operatoren en stringmanipulatie hebbengeleerd, zullen we
# deze vaardigheden gebruiken om dit programma te creëren.

# Final Design
# Het is altijd goed om een beeld te vormen van wat je probeert te bouwen. Voor grotere projecten
# wil je een stroomdiagram of een soort ontwerpdocument maken dat je op koers houdt. Op deze manier
# wijkt je niet af van het beoogde resultaat. Voor ons zullen we een klein programma voor het
# printen van bonnetjes bouwen met de concepten die we hebben geleerd, waarbij de output eruit zal
# zien als de volgende figuur.

amount = 50
enclosedIn = "*"
middlePart = "="
startEnd = (amount*enclosedIn)+"\n"
middle = (amount*middlePart)+"\n"

# Address part
name = "\t\tCoding Temple, Inc."
street = "283 Franklin St."
city = "Boston, MA"
next = "\n\t\t"
address = f"{name}{next}{street}{next}{city}\n"

# Products
tableHead = "\tProduct Name\tProduct Price"
product1 = "\tBooks\t\t$49.95"
product2 = "\tComputer\t$579.99"
product3 = "\tMonitor\t\t124.89"
products = f"{tableHead}\n{product1}\n{product2}\n{product3}\n"

# Total
total = "\t\t\tTotal\n\t\t\t$754.83\n"

# Ending Sequence
thanks = "Thanks for shopping with us today!"
end = f"\n\t{thanks}\n\n{startEnd}"

print(startEnd+address+middle+products+middle+total+middle+end)

# Extra
# Opdracht maak een programma dat de bovenstaande uitvoer afdrukt. Als dat gelukt is Voeg dan ook *
# die zowel boven als onder de uitvoer staan toe aan de linker en de rechterkant van elke regel.  

next = "\t\t *\n*\t\t"
address = f"*{name}{next}{street}{next}{city}\t\t\t *\n"
products = f"*{tableHead}\t\t *\n*{product1}\t\t\t *\n*"
products += f"{product2}\t\t\t *\n*{product3}\t\t\t *\n"
total = "*\t\t\tTotal\t\t\t *\n*\t\t\t$754.83\t\t\t *\n"
empty = "*\t\t\t\t\t\t *\n"
end = f"{empty}*\t{thanks}\t *\n{empty}{startEnd}"

print(startEnd+address+middle+products+middle+total+middle+end)