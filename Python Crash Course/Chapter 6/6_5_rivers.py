# 6-5. Rivers: Make a dictionary containing three major rivers
# and the country each river runs through. One key-value pair
# might be 'nile': 'egypt'.

rivers = {
    'Nile': 'Egypt',
    'Rhine': 'The Netherlands, Germany and Swiss',
    'Meuse' : 'The Netherlands, Belgium and France'
}

# 1) Use a loop to print a sentence about each river, such as
# The Nile runs through Egypt.

for key, value in rivers.items():
    print(f"The {key} runs through {value}.")
print()

# 2) Use a loop to print the name of each river included in
# the dictionary.

for key in rivers.keys():
    print(key)
print()

# 3) Use a loop to print the name of each country included
# in the dictionary.

for value in rivers.values():
    print(value)