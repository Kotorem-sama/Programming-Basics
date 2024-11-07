# Vraag de gebruiker om hun leeftijd in te voeren.
# Afhankelijk van hun invoer, geef een van de volgende
# groepen weer: 
# a. Tussen 0 en 12 = "Kind" 
# b. Tussen 13 en 19 = "Tiener" 
# c. Tussen 20 en 30 = "Jongvolwassene" 
# d. Tussen 31 en 64 = "Volwassene"
# e. 65 of ouder = "Senior"

leeftijd = int(input("Wat is je leeftijd? "))

if leeftijd >= 0 and leeftijd < 13:
    print("Kind")
elif leeftijd > 12 and leeftijd < 20:
    print("Tiener")
elif leeftijd > 19 and leeftijd < 31:
    print("Jongvolwassene")
elif leeftijd > 30 and leeftijd < 65:
    print("Volwassene")
elif leeftijd > 64:
    print("Senior")