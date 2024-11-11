# Opdracht 4 Tekstgebaseerd RPG (Role Play Game)
# Dit is een open opdracht. Creëer een tekstgebaseerd RPG
# met een verhaallijn. Je neemt invoer van de gebruiker en
# geeft ze een paar keuzes, en afhankelijk van wat ze kiezen,
# kunnen ze een ander pad volgen. Je zult meerdere
# vertakkingsverklaringen gebruiken, afhankelijk van de lengte
# van het verhaal.

import os

def keuzes(keuze, keuze_1, keuze_2):
    if keuze == "1":
        keuze_1()
    elif keuze == "2":
        keuze_2()
    else:
        end_game()

def start_game_tekst():
    os.system('cls')
    print("Je bevindt je in een donker bos. Er zijn twee paden voor je.")
    print("Keuzes:\n1. Links\n2. Rechts\n3. Stop het spel")

def links_pad_tekst():
    os.system('cls')
    print("Je loopt het linker pad op en hoort een vreemd geluid.")
    print("Voor je zie je een hut. Wat wil je doen?")
    print("Keuzes:\n1. Ga naar binnen\n2. Loop door\n3. Stop het spel")

def rechts_pad_tekst():
    os.system('cls')
    print("Je kiest het rechter pad en komt bij een grote rivier.")
    print("Er is een boot, maar deze ziet er gammel uit.")
    print("Keuzes:\n1. Probeer de rivier over te steken met de boot")
    print("2. Loop langs de rivier\n3. Stop het spel")

def hut_tekst():
    os.system('cls')
    print("Je gaat de hut binnen en ziet een oude man.")
    print("Hij biedt je een drankje aan.")
    print("Keuzes:\n1. Accepteer het drankje\n2. Weiger en loop weg\n3. Stop het spel")

def boot_tekst():
    os.system('cls')
    print("De boot begint te zinken halverwege de rivier.")
    print("Keuzes:\n1. Spring in het water en zwem")
    print("2. Blijf in de boot\n3. Stop het spel")

def start_game():
    start_game_tekst()    
    keuze = input("Welke keuze maak je? (1, 2 of 3): ")

    while keuze not in ['1', '2', '3']:
        start_game_tekst()
        keuze = input("Ongeldige keuze, probeer opnieuw.\n(1, 2 of 3): ")

    keuzes(keuze, links_pad, rechts_pad)

def links_pad():
    links_pad_tekst()
    keuze = input("Welke keuze maak je? (1, 2 of 3): ")
    
    while keuze not in ['1', '2', '3']:
        links_pad_tekst()
        keuze = input("Ongeldige keuze, probeer opnieuw.\n(1, 2 of 3): ")
    
    keuzes(keuze, hut, rivier)

def rechts_pad():
    rechts_pad_tekst()
    keuze = input("Welke keuze maak je? (1, 2 of 3): ")

    while keuze not in ['1', '2', '3']:
        rechts_pad_tekst()
        keuze = input("Ongeldige keuze, probeer opnieuw.\n(1, 2 of 3): ")

    keuzes(keuze, boot, berg)

def hut():
    hut_tekst()
    keuze = input("Welke keuze maak je? (1, 2 of 3): ")

    while keuze not in ['1', '2', '3']:
        hut_tekst()
        keuze = input("Ongeldige keuze, probeer opnieuw.\n(1, 2 of 3): ")

    keuzes(keuze, toverkracht, weg_kwijt)

def toverkracht():
    os.system('cls')
    print("Het drankje blijkt een toverdrank te zijn! Je krijgt superkrachten.")
    print("Gefeliciteerd! Je hebt een positief einde bereikt!")

def weg_kwijt():
    os.system('cls')
    print("Je loopt weg, maar je verliest je weg in het bos.")
    print("Helaas, je hebt een negatieve einde bereikt.")

def rivier():
    os.system('cls')
    print("Je loopt langs de rivier en vindt een schat begraven onder een boom.")
    print("Gefeliciteerd! Je hebt een schat gevonden en het spel gewonnen!")
    

def boot():
    boot_tekst()
    keuze = input("Welke keuze maak je? (1, 2 of 3): ")

    while keuze not in ['1', '2', '3']:
        boot_tekst()
        keuze = input("Ongeldige keuze, probeer opnieuw.\n(1, 2 of 3): ")

    keuzes(keuze, overkant, verdrinken)

def overkant():
    os.system('cls')
    print("Je zwemt veilig naar de overkant.")
    print("Gefeliciteerd! Je hebt het avontuur overleefd!")

def verdrinken():
    os.system('cls')
    print("De boot zinkt en je verdrinkt.")
    print("Helaas, je hebt het negatieve einde bereikt.")

def berg():
    os.system('cls')
    print("Je loopt langs de rivier en komt bij een berg.")
    print("Bovenop zie je een prachtig uitzicht over het bos.")
    print("Gefeliciteerd! Je hebt een vredig einde bereikt en het spel gewonnen!")

def end_game():
    os.system('cls')
    print("Het spel is gestopt.")

start_game()