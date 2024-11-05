# 5-1. Conditional Tests: Write a series of conditional tests.
# Print a statement describing each test and your prediction
# for the results of each test. Your code should look
# something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 2) Create at least 10 tests. Have at least 5 tests evaluate to
# True and another 5 tests evaluate to False.

number = 2
print("\nIs number == '2'? I predict True.")
print(number == 2)

print("\nIs number == '5'? I predict False.")
print(number == 5)

bike = "Electrical"
print("\nIs bike == 'Electrical'? I predict True.")
print(bike == "Electrical")

print("\nIs bike == 'electrical'? I predict False.")
print(bike == "electrical")

bike = "Electrical"
print("\nIs bike.lower() == 'electrical'? I predict True.")
print(bike.lower() == "electrical")

print("\nIs bike.lower() == 'Electrical'? I predict False.")
print(bike.lower() == "Electrical")

number = 23
print("\nIs number <= '23'? I predict True.")
print(number <= 23)

print("\nIs number < '23'? I predict False.")
print(number < 23)