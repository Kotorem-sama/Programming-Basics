# 6-7. People: Start with the program you wrote for Exercise
# 6-1 (page 98). Make two new dictionaries representing
# different people, and store all three dictionaries in a
# list called people. Loop through your list of people. As
# you loop through the list, print everything you know about
# each person.

person_1 = {
    'first_name' : "Jori",
    'last_name' : "van Noor",
    'age' : 27,
    'city' : "The Hague"
}

person_2 = {
    'first_name' : "Sharon",
    'last_name' : "Larochelle",
    'age' : 25,
    'city' : "Rotterdam"
}

person_3 = {
    'first_name' : "Claudia",
    'last_name' : "Roelink",
    'age' : 37,
    'city' : "Venlo"
}

people = [ person_1, person_2, person_3 ]

for person in people:
    print(f"""{person['first_name']} {
        person['last_name']} is {
            person['age']} years old, and lives in {
                person['city']}.""")