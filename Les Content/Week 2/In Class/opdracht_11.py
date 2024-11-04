# 11. Display een bar-chart van de list:
# numbers = [19, 3, 15, 7, 11]
# Index      Value Bar
#     0         19 *******************
#     1          3 ***
#     2         15 ***************
#     3          7 *******
#     4         11 ***********

numbers = [19, 3, 15, 7, 11]

print("Index\tValue\tBar")
for i in range(0, len(numbers)):
    print(f"{i}\t{numbers[i]}\t{numbers[i]*"*"}")