#7. Schrijf een programma om het volgende patroon te construeren,
# met behulp van een geneste for-loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

character = "*"
character += " "
length = 5

for i in range(1,length+1):
    print(character*i)
    if i == length:
        for j in range(length-1, 0, -1):
            print(character*j)