# Loops

# while loop

i = 0
while i < 10:
    print(i)
    i += 2

print('After while loop')

print('-' * 60)

# Data structures / collections

# Tuple
# index/key 0        1     2
my_tuple = ('Piotr', 'GG', 182)
print(my_tuple)
print( my_tuple[2] )
print( my_tuple[0] )
# print( my_tuple[5] )  # KO: IndexError: tuple index out of range

#           0       1                2
#            0  1    0    1    2      0     1
my_tuple = ((1, 2), ('a', 'b', 'c'), (True, False))
print(my_tuple)
print( my_tuple[1] )
print( my_tuple[1][1] )

print('-' * 60)

# index     0    1    2    3    4    5    6    7    8    9
my_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
# -index    -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

print(my_tuple)
print(my_tuple[5])
print(my_tuple[-5])
print(my_tuple[0])
print(my_tuple[-10])
print(my_tuple[-1])

print('-' * 60)

# index     0    1    2    3    4    5    6    7    8    9
my_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
# -index    -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

print(my_tuple)
print(my_tuple[0])
# left-closed, right-opened - left is included, right is not
print(my_tuple[1:3])  # b, c
print(my_tuple[5:9])  # f, g, h, i

# [start:stop] - we can skip start and/or stop
print(my_tuple[5:])  # 'f', 'g', 'h', 'i', 'j'
print(my_tuple[:4])  # 'a', 'b', 'c', 'd'
print(my_tuple[:])  # 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'

print(my_tuple[2:-3])  # 'c', 'd', 'e', 'f', 'g'
print(my_tuple[-4:])  # 'g', 'h', 'i', 'j'

# [start:stop:step] - step can be positive or negative
print(my_tuple[0:8:2])  # 'a', 'c', 'e', 'g'
print(my_tuple[::2])  # 'a', 'c', 'e', 'g', 'i'
print(my_tuple[::-2])  # 'j', 'h', 'f', 'd', 'b'
print(my_tuple[::-1])







