# 10-7. Addition Calculator: Wrap your code from Exercise
# 10-5 in a while loop so the user can continue entering
# numbers, even if they make a mistake and enter text
# instead of a number.

print("Enter 'q' at any time to quit.\n")

while True:
    try:
        first_number = input("\nWhat is the first number? ")
        if first_number == 'q':
            break
        else:
            first_number = int(first_number)
        
        second_number = input("What is the second number? ")
        if second_number == 'q':
            break
        else:
            second_number = int(second_number)

    except ValueError:
        print("Please input a number.")
    else:
        sumtext = f"{first_number} + {second_number}"
        sum = first_number + second_number
        print(f"The result of {sumtext} = {sum}")