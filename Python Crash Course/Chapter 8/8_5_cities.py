# 8-5. Cities: Write a function called describe_city() that
# accepts the name of a city and its country. The function
# should print a simple sentence, such as Reykjavik is in
# Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one
# of which is not in the default country.

def describe_city(name, country="a country on earth"):
    print(f"{name.title()} is in {country.title()}")

describe_city("The Hague", "The Netherlands")
describe_city("Reykjavik", "Iceland")
describe_city("New York City")