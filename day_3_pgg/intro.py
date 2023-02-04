# iterable - an object we can iterate through

# range - creates an objects that returns integers from specified range
# by default: start = 0, step = 1
for number in range(11):
    print(number)

print('-' * 10)

# by default: step = 1
for number in range(-10, 11):
    print(number)

print('-' * 10)

for number in range(-10, 11, 2):
    print(number)


print('-' * 30)


# unpacking
# number of elements on the right side
# must match the number of variables you assign them to
my_tuple = ('Piotr', 'GG')
first_name, last_name = my_tuple
print(first_name, last_name)

first_name, last_name = ('Piotr', 'GG')
print(first_name, last_name)

# first_name, last_name = ('Piotr', 'GG', 10)  # KO: ValueError: too many values to unpack (expected 2)

print('-' * 30)

# enumarate
#        0      1      2        3
names = ['Tom', 'Ann', 'Chris', 'Peter']

for name in names:
    print(name)

print('-' * 10)

for name in enumerate(names):
    # now in name we have a tuple
    # enumarate returns for each iteration a tuple
    # with number (index) and the value
    print(name, name[0], name[1])

print('-' * 10)

# we can use unpacking to make that more convenient
for index, name in enumerate(names):
    print(index, name)

print('-' * 10)

# we can say from which number enumerate should count
# by default it is 0
for num, name in enumerate(names, start=1):
    print(f"{num}. {name}")
