# 2-7. Stripping Names: Use a variable to represent a person’s
# name, and include some whitespace characters at the
# beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.

name = "\n     Rick Slingerland   \t"

# Print the name once, so the whitespace around the name is
# displayed. Then print the name using each of the three
# stripping functions, lstrip(), rstrip(), and strip().

print(f"1.'{name.lstrip()}'")
print(f"2.'{name.rstrip()}'")
print(f"3.'{name.strip()}'")