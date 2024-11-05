# 4-5. Summing a Million: Make a list of the numbers from one
# to one million, and then use min() and max() to make sure
# your list actually starts at one and ends at one million.
# Also, use the sum() function to see how quickly Python can
# add a million numbers.

mil = list(range(1, 1000001))

# Formatted it so it's readable with commas as seperator
print("{:,}".format(min(mil)))
print("{:,}".format(max(mil)))
print("{:,}".format(sum(mil)))