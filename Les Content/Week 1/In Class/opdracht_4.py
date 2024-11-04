# Schrijf een Python-programma dat uit twee gegeven strings één enkele string maakt, gescheiden door een spatie, en de eerste twee tekens van elke string omwisselt.
 
# Sample:
# String1 = 'abc'
# String2 = 'xyz'

# Expected Result : 'xyc abz'

s1 = 'abc'
s2 = 'xyz'
s3 = s2[:2] + s1[-1]
s4 = s1[:2] + s2[-1]
print(s3, s4)