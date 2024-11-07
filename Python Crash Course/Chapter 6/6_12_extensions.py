# 6-12. Extensions: We’re now working with examples that are
# complex enough that they can be extended in any number of
# ways. Use one of the example programs from this chapter,
# and extend it by adding new keys and values, changing the
# context of the program, or improving the formatting of the
# output.

favorite_numbers = {
    'Tirsa' : [500000001, 500000002, 500000003],
    'Rick' : [89],
    'Nick' : [69, 6969, 696969],
    'Luuk' : [42,420],
    'Alisa' : [5, 55, 555, 5555, 55555],
    'Truus' : [22, 189, 101, 47, 11],
    'Balder' : [19, 182281, 222, 2812],
    'Veerle' : [123, 456, 789, 0]
}

for key, value in favorite_numbers.items():
    listOfNumbers = ", ".join(str(i) for i in value)
    print(f"{key}'s favorite numbers are {listOfNumbers}.")