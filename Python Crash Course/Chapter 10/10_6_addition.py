# 10-6. Addition: One common problem when prompting for
# numerical input occurs when people provide text instead of
# numbers. When you try to convert the input to an int,
# you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch
# the ValueError if either input value is not a number, and
# print a friendly error message. Test your program by
# entering two numbers and then by entering some text instead
# of a number.

try:
    first_number = int(input("What is the first number? "))
    second_number = int(input("What number do you want to add? "))
except ValueError:
    print("You can't enter letters!")
else:
    sum = f"{first_number} + {second_number}"
    print(f"The result of {sum} = {first_number + second_number}")
