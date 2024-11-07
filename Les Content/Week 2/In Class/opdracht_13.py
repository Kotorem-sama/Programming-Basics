# 13. Schrijf een functie om de Fibonacci-reeks tussen 0 en n te krijgen (n is een gebruikersinvoernummer kleiner dan 60).
# De Fibonacci-reeks is: 1, 1, 2, 3, 5, 8, 13, 21, ....

def fibonacci(end):
    if end > 60 or end < 1:
        print("Nummer is niet binnen de 1 en 60")
    else:
        reeks = [1, 1]
        while reeks[-1]+reeks[-2] < end:
            reeks.append(reeks[-1]+reeks[-2])
        print(reeks)

invoer = input("Geef een nummer: ")
try:
    invoer = int(invoer)
    fibonacci(invoer)
except:
    print("Dat is geen nummer!")