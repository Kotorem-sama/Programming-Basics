# 10. a. Schrijf een programma met de functie maximum(n1, n2, n3)
# die drie gehele getallen als parameters ontvangt en het
# grootste van deze getallen retourneert.

def maximum(n1, n2, n3):
    return max(n1, n2, n3)

print(maximum(2, 8, 6))

# b. Pas de functie maximum aan zodat deze een variabel aantal
# getallen als parameter accepteert.

def maximum2(*n):
    return max(n)

print(maximum2(2, 8, 3, 9, 1, 12))