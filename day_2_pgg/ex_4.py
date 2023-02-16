"""
Create a tuple containing 10 different integers. Using the indexing operator, get:

- second element (20)
- next to last item (90)
- items three to seven (inclusive) (30, 40, 50, 60, 70)
- every third element (10, 40, 70, 100)
- every second element counting from the end (100, 80, 60, 40, 20)
"""

#    0   1   2   3   4   5   6   7   8   9 -> keys/indexes
x = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
#    1   2   3   4   5   6   7   8   9   10 -> which elements
#   -10  -9  -8  -7  -6  -5  -4  -3  -2  -1 -> negative indexes

print(x[1])
print(x[-2])
print(x[2:7])
print(x[::3])
print(x[::-2])
