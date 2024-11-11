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

def heads_or_tails(random):
    outcomes = { 'heads': 0, 'tails': 0 }
    sides = list(outcomes.keys())

    for i in range(10000):
        outcomes[random.choice(sides)] += 1
    
    return outcomes

print('Default initializiation:\n')

for tries in range(5):
    outcomes = heads_or_tails(random.SystemRandom())
    print(f'Heads: {outcomes['heads']}\t Tails: {outcomes['tails']}')

print('\nSame seed:\n')

seed = time.time()

for tries in range(5):
    outcomes = heads_or_tails(random.SystemRandom(seed))
    print(f'Heads: {outcomes['heads']}\t Tails: {outcomes['tails']}')

# Conclusion: Doesnt make a single difference to use either.
# Both outcomes are random, so it doesn't matter whether you
# use a seed or not. It was supposed to show how with a seed
# the random output could be determined, however this doesn't
# seem to be the case.