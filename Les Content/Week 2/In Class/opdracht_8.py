# 8. Schrijf en test een Python-functie om de even getallen
# uit een gegeven lijst af te drukken.

Voorbeeldlijst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even(lijst):
    result = []

    for i in lijst:
        if i % 2 == 0:
            result.append(i)
    return result

def even2(lijst):
    return [i for i in lijst if i%2==0]

print(f"Slow: {even(Voorbeeldlijst)}")
print(f"Fast: {even2(Voorbeeldlijst)}")