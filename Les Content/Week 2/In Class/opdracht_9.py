# 9. Schrijf een Python-functie die controleert of een
# doorgegeven string een palindroom is of niet. Een palindroom
# is een woord die achterwaarts en # voorwaarts hetzelfde leest,
# bijvoorbeeld madam.

def isPalindroom(s1):
    s1 = s1.lower()
    return s1 == s1[::-1]

print(isPalindroom("Madam"))
print(isPalindroom("wowa"))