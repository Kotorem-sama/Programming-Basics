# 6-11. Cities: Make a dictionary called cities. Use the names
# of three cities as keys in your dictionary. Create a
# dictionary of information about each city and include the
# country that the city is in, its approximate population, and
# one fact about that city. The keys for each city’s
# dictionary should be something like country, population,
# and fact. Print the name of each city and all of the
# information you have stored about it.

cities = {
    'Zoetermeer' : {
        'Country' : 'The Netherlands',
        'Population' : 125267,
        'Fact' : 'Zoetermeer got its name from the river \'Zoete\''
    },
    'The Hague' : {
        'Country' : 'The Netherlands',
        'Population' : 549163,
        'Fact' : 'The Hague\'s Gothic-style Binnenhof (or Inner Court) complex is the seat of the Dutch parliament.'
    },
    'Rotterdam' : {
        'Country' : 'The Netherlands',
        'Population' : 664311,
        'Fact' : 'Rotterdam has a bigger population than Amsterdam (the capitol of The Netherlands).'
    }
}

for key, value in cities.items():
    print(f"{key} is a city in {
        value['Country']} with a population of {
        value['Population']}.\nHere's a fact: {value['Fact']}")