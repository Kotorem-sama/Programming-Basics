# Here is my name, but with a lot of whitespaces and useless tabs and enters
name = "\n     Rick Slingerland   \t"

# Prints the name but removes all whitespaces on the left.
print(f"1.'{name.lstrip()}'")
# Prints the name but removes all whitespaces on the right.
print(f"2.'{name.rstrip()}'")
# Prints the name but removes all whitespaces.
print(f"3.'{name.strip()}'")