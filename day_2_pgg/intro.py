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

print('-' * 60)

# useful methods, to be not only on tuple but also
# (in most cases) on other collections as well
print(len(my_tuple))  # how many elements we have in a collection
print('a' in my_tuple)
print('q' in my_tuple)
print('q' not in my_tuple)

# my_tuple[0] = -10  # KO: TypeError: 'tuple' object does not support item assignment

#          0   1   2   3   4
numbers = (10, 20, 30, 40, 50)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sum(numbers) / len(numbers))

print(numbers.index(40))  # 3
print(numbers.count(40))

print('-' * 60)

# Lists
my_list = [10, 20, 30, 40, 50]
print(my_list)

# [] - index operator works exactly the same as in tuples
print(my_list[1])

print(my_list)
my_list[0] = 11
print(my_list)

# tuple: (Piotr, GG, 182, 46)
# list:  [10, 12, -5, 17] - different temperatures

print(my_list)
my_list.append(60)
print(my_list)

my_list.insert(1, 12)
print(my_list)

my_list[0:2] = [1, 2]
print(my_list)

my_list[0:2] = [1, 2, 3, 4]  # we are replacing first two elements and adding rest
print(my_list)

my_list.extend([700, 800, 900])
print(my_list)

# my_list.append([700, 800, 900])
# print(my_list)

# deleting elements by index
del(my_list[0])  # here we can use all the features of the indexing operator (start, stop, step)
print(my_list)

# after the deletion elements are reindex
del(my_list[0:3])
print(my_list)

# delete element by its value
my_list.remove(800)
print(my_list)

print('-' * 60)

# iterating through collections...

print(my_list)
print()

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

print('-' * 3)

# for loop
for number in my_list:
    print(number)
