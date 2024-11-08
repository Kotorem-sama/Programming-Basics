# 2-11. Adding Comments: Choose two of the programs you’ve
# written, and add at least one comment to each. If you don’t
# have anything specific to write because your programs are
# too simple at this point, just add your name and the current
# date at the top of each program file. Then write one
# sentence describing what the program does.

# Here is my name, but with a lot of whitespaces and useless
# tabs and enters
name = "\n     Rick Slingerland   \t"

# Prints the name but removes all whitespaces on the left.
print(f"1.'{name.lstrip()}'")
# Prints the name but removes all whitespaces on the right.
print(f"2.'{name.rstrip()}'")
# Prints the name but removes all whitespaces.
print(f"3.'{name.strip()}'")