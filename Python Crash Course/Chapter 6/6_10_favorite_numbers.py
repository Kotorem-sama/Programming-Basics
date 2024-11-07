# 6-10. Favorite Numbers: Modify your program from Exercise
# 6-2 (page 98) so each person can have more than one
# favorite number. Then print each person’s name along
# with their favorite numbers.

favorite_numbers = {
    'Tirsa' : [500000001, 500000002, 500000003],
    'Rick' : [89],
    'Nick' : [69, 6969, 696969],
    'Luuk' : [42,420],
    'Alisa' : [5, 55, 555, 5555, 55555]
}

for key, value in favorite_numbers.items():
    print(f"{key}'s favorite numbers are:")
    for number in value:
        print(number)
    print()