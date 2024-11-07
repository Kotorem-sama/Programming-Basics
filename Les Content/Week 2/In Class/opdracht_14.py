# 14. Schrijf een Python-programma dat een string accepteert en het aantal cijfers en letters berekent.
# Sample Data : Python 3.2
# Expected Output : 
# Letters 6
# Digits 2

def counter(input_string):
    letters = 0
    digits = 0
    for karakter in input_string:
        if karakter.lower() in 'abcdefghijklmnopqrstuvwxyz':
            letters += 1
        elif karakter in '1234567890':
            digits += 1

    print(f"Letters {letters}\nDigits {digits}")

counter("ThisisAtest!2182")