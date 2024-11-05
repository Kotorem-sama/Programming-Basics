# 5-2. More Conditional Tests: You don’t have to limit the
# number of tests you create to 10. If you want to try more
# comparisons, write more tests and add them to
# conditional_tests.py. Have at least one True and one False
# result for each of the following:

# 1) Tests for equality

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#  and inequality with strings

car = 'audi'
print("\nIs car != 'subaru'? I predict True.")
print(car != 'subaru')

print("\nIs car != 'audi'? I predict False.")
print(car != 'audi')

# 2) Tests using the lower() method

bike = "Electrical"
print("\nIs bike.lower() == 'electrical'? I predict True.")
print(bike.lower() == "electrical")

print("\nIs bike.lower() == 'Electrical'? I predict False.")
print(bike.lower() == "Electrical")

# 3) Numerical tests involving equality

number = 5
print("\nIs number == '2'? I predict True.")
print(number == 5)

print("\nIs number == '5'? I predict False.")
print(number == 2)

# and inequality,

number = 2
print("\nIs number != '3'? I predict True.")
print(number != 3)

print("\nIs number != '2'? I predict False.")
print(number != 2)

# greater than

number = 7
print("\nIs number > '3'? I predict True.")
print(number > 3)

print("\nIs number > '20'? I predict False.")
print(number > 20)

# and less than,

number = 2
print("\nIs number < '3'? I predict True.")
print(number < 3)

print("\nIs number < '1'? I predict False.")
print(number < 1)

# greater than or equal to,

number = 78
print("\nIs number >= '78'? I predict True.")
print(number >= 78)

print("\nIs number >= '79'? I predict False.")
print(number >= 79)

# and less than or equal to

number = 23
print("\nIs number <= '23'? I predict True.")
print(number <= 23)

print("\nIs number <= '22'? I predict False.")
print(number <= 22)

# 4) Tests using the 'and' keyword

number = 5
print("\nIs number > '0' and number < '10'? I predict True.")
print(number > 0 and number < 10)

print("\nIs number > '0' and number < '5'? I predict False.")
print(number > 0 and number < 5)

# and the 'or' keyword

number = 5
print("\nIs number > '10' or number < '6'? I predict True.")
print(number > 10 or number < 6)

print("\nIs number > '15' or number < '5'? I predict False.")
print(number > 15 or number < 5)

# 5) Test whether an item is in a list

numbers = list(range(5, 150, 5))
print("\nIs '100' in numbers? I predict True.")
print(100 in numbers)

print("\nIs '150' in numbers? I predict False.")
print(150 in numbers)

# 6) Test whether an item is not in a list

numbers = list(range(5, 150, 5))
print("\nIs '150' not in numbers? I predict True.")
print(150 not in numbers)

print("\nIs '100' not in numbers? I predict False.")
print(100 not in numbers)