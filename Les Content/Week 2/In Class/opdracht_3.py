# Met het lijst sample = [[2, 5], [1, 2], [4, 4], [2, 3], [2, 1]]
# schrijf een programma dat afdrukt:

sample = [[2, 5], [1, 2], [4, 4], [2, 3], [2, 1]]

# a) het eerste en het laatste element in de lijst
print(sample[0], sample[-1])

# b) het eerste element van het tweede element in de lijst
print(sample[1][0])

# c) vervang het eerste element van het laatste element in de lijst door de waarde "zwart"
sample[-1][0] = "zwart"
print(sample)

# d) het kleinste aantal van de elementen 2 en 3 in de lijst
small = sample[1][0]
for i in range(1, 3):
    for j in sample[i]:
        if j < small:
            small = j

print(small)