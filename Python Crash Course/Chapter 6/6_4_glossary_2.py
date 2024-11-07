# 6-4. Glossary 2: Now that you know how to loop through a
# dictionary, clean up the code from Exercise 6-3 (page 99)
# by replacing your series of print() calls with a loop that
# runs through the dictionary’s keys and values. When you’re
# sure that your loop works, add five more Python terms to
# your glossary. When you run your program again, these new
# words and meanings should automatically be included in the
# output.

glossary = {
    "list" : "a type of list that contains values, but can also contain other lists",
   "string" : "a type of value that contains characters strung together.",
   "integer" : "a type of value that contains numbers without decimals.",
   "boolean" : "a type of value that can be either True or False, just as the outcome of a conditional test.",
   "float" : "a type of value that contains numbers with decimal numbers.",
   "dictionary" : "a type of list that combinds keys with values.",
   "tuple" : "a sort of list that contains values, but the values cannot be changed.",
   "print command" : "a command that outputs inserted text in the python console.",
   "append function" : "a function that adds an inserted value to the end of a list.",
   "pop function" : "a function that removes the last item in a list."
}

for key, value in glossary.items():
    print(f"A {key} is {value}")