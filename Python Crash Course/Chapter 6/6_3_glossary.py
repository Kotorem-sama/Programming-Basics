# 6-3. Glossary: A Python dictionary can be used to model an
# actual dictionary. However, to avoid confusion, let’s call
# it a glossary.

# 1) Think of five programming words you’ve learned about in
# the previous chapters. Use these words as the keys in your
# glossary, and store their meanings as values.

glossary = {
    "list" : "a type of list that contains values, but can also contain other lists",
   "string" : "a type of value that contains characters strung together.",
   "integer" : "a type of value that contains numbers without decimals.",
   "boolean" : "a type of value that can be either True or False, just as the outcome of a conditional test.",
   "float" : "a type of value that contains numbers with decimal numbers."
}

# 2) Print each word and its meaning as neatly formatted
# output. You might print the word followed by a colon and then
# its meaning, or print the word on one line and then print its
# meaning indented on a second line. Use the newline character
# (\n) to insert a blank line between each word-meaning pair
# in your output.

print(f"A list is {glossary['list']}")
print(f"A string is {glossary['string']}")
print(f"A integer is {glossary['integer']}")
print(f"A boolean is {glossary['boolean']}")
print(f"A float is {glossary['float']}")