# 5-6. Stages of Life: Write an if-elif-else chain that
# determines a person’s stage of life. Set a value for the
# variable age, and then:
# 1) If the person is less than 2 years old, print a message
# that the person is a baby.
# 2) If the person is at least 2 years old but less than 4,
# print a message that the person is a toddler.
# 3) If the person is at least 4 years old but less than 13,
# print a message that the person is a kid.
# 4) If the person is at least 13 years old but less than 20,
# print a message that the person is a teenager.
# 5) If the person is at least 20 years old but less than 65,
# print a message that the person is an adult.
# 6) If the person is age 65 or older, print a message that
# the person is an elder.

age = 200

if age >= 0 and age < 2:
    print("This person is a baby.")
elif age >= 2 and age < 4:
    print("This person is a toddler")
elif age >= 4 and age < 13:
    print("This person is a kid")
elif age >= 13 and age < 20:
    print("This person is a teenager")
elif age >= 20 and age < 65:
    print("This person is an adult")
elif age >= 65:
    print("This person is an elder")
else:
    print("Someone can't be negative age")