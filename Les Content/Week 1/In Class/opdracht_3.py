# Schrijf een Python-programma dat een string bewerkt door alle voorkomens van het eerste teken te vervangen door '$', met uitzondering van het eerste teken zelf.
 
# Sample String : 'restart'
# Expected Result : 'resta$t'

s = "restart"
first = s[0]
print(f"{first}{s[1:].replace(first, "$")}")