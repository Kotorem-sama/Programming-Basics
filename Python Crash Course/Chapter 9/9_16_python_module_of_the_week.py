# 9-16. Python Module of the Week: One excellent resource for
# exploring the Python standard library is a site called
# Python Module of the Week. Go to https://pymotw.com and look
# at the table of contents. Find a module that looks
# interesting to you and read about it, perhaps starting
# with the random module.

# Some operating systems provide a random number generator
# that has access to more sources of entropy that can be
# introduced into the generator. random exposes this feature
# through the SystemRandom class, which has the same API as
# Random but uses os.urandom() to generate the values that
# form the basis of all of the other algorithms.

import random
import time

print('Default initializiation:\n')

r1 = random.SystemRandom()
r2 = random.SystemRandom()

for i in range(3):
    print('{:04.3f}  {:04.3f}'.format(r1.random(), r2.random()))

print('\nSame seed:\n')

seed = time.time()
r1 = random.SystemRandom(seed)
r2 = random.SystemRandom(seed)

for i in range(3):
    print('{:04.3f}  {:04.3f}'.format(r1.random(), r2.random()))