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

print('-' * 30)

# strings are iterable
#            0123456789
my_string = 'To be or not to be'

for character in my_string:
    print(character)

print('-' * 30)

# strings support indexing operator
# works exactly the same as for tuples and lists
print(my_string[0])
print(my_string[1:5])
print(my_string[1:10:2])
print(my_string[-1])
print(my_string[::-1])

print('-' * 30)

# once created string doesn't change
print(my_string.lower())  # converts all characters to lower case and returns a new string
print(my_string)  # the original string is not changed, stays the same
print("hello world".upper())
print(my_string.title())
print(my_string.capitalize())

print(my_string.split())  # by default split uses space as divider
print(my_string.split(' '))
print(my_string.split('o'))

names = ['Tom', 'Jane', 'John']
print(';'.join(names))
print('<->'.join(names))

print(my_string.count('o'))
print(my_string.replace('o', '*'))
print(my_string.replace('To', '**'))

print(my_string)
# is 'to' in my_string? True
print('to' in my_string)

print('-' * 30)

"""
Dictionary
https://realpython.com/python-dicts/

Python dictionary consists of keys and values
What can be a key:
- the most popular approach is to use strings as keys
- but other data types can be keys as well, for example:
    integers, floats, bools, tuples
  as rule of thumb only immutable data types can be dictionary keys 
What can be a value:
- any data type in python can be a value of a dictionary
"""
my_dict = {
    # key       : value
    'first_name': 'Piotr',
    'last_name': 'GG',
    'shoe_number': 46,
    'favourite_numbers': [1, 2, 3, 4, 5],
}

# my_dict[key]
print(my_dict['first_name'])
print(my_dict['favourite_numbers'])
print(my_dict['favourite_numbers'][1])
my_dict['first_name'] = 'Peter'
print(my_dict)

my_dict['height'] = 180
print(my_dict)

# we are checking if dictionary contains a key
print('height' in my_dict)  # True
print('weight' in my_dict)  # False

print('-' * 10)

# iterating through dictionary
# by default iterating through keys
for key in my_dict:
    print(key, my_dict[key])

print('-' * 10)

# .items() for each iteration will return a tuple
for key, value in my_dict.items():
    print(key, value)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

del(my_dict['height'])
print(my_dict)
# by default if the key is not present in the dictionary KeyError exception is raised
# print(my_dict['height'])  # KO: KeyError: 'height'
print(my_dict.get('height'))  # Instead of exception, if key is not present we get None
print(my_dict.get('height', -1))  # We can define the default value returned if the key is not present

print('-' * 30)

# Set
my_set = {10, 20, 30, 40, 50}

print(my_set)
my_set.add(10)
print(my_set)
my_set.add(60)
print(my_set)

my_set.remove(60)
print(my_set)

# indexing operator [] does NOT work!!!
# my_set[0]  # KO: TypeError: 'set' object is not subscriptable

print(len(my_set))

for number in my_set:
    print(number)

# quickly removing duplicates from a list
# caveat: with conversion to set we loose the order of the elements

my_list = [1, 1, 1, 1, 2, 3]
print(my_list)
my_set = set(my_list)
print(my_set)
my_list = list(my_set)
print(my_list)

print('-' * 30)

a = {1, 2, 3}
b = {1, 2, 4, 5}

print(a)
print(b)

# operations based on a set theory
# https://commons.wikimedia.org/wiki/File:Set_Theory_Operations.svg
# sum, union
print(a.union(b))

# intersection
print(a.intersection(b))

# symmetric difference
print(a.symmetric_difference(b))

# difference
print(a.difference(b))

print('-' * 30)

# it's easy to convert one collection into another
my_set = {1, 1, 1, 1, 2, 3, 4}
list_from_set = list(my_set)
print(my_set)
print(list_from_set)

print('-' * 10)

# we can convert any iterable to a collection
my_list = list(range(-5, 6))
print(my_list)

print('-' * 30)

# Comprehensions
# list comprehensions

numbers = []
for number in range(0, 11):
    numbers.append(number)

print(numbers)

# the same thing but with list comprehension
numbers = [number for number in range(0, 11)]
print(numbers)

# [expression for local_variable in iterable]
numbers = [number * 10 for number in range(0, 11)]
print(numbers)


# set comprehensions
my_string = "To be or not to be"
characters = {character for character in my_string}
print(my_string)
print(characters)

# dict comprehension
my_string = "To be or not to be"
occurences = {letter: letter.upper() for letter in my_string}
print(occurences)
#        key :  value
words = {word: len(word) for word in my_string.split(' ')}
print(words)

print('-' * 30)

salaries = [1000, 2000, 2500, 1500, 5000]
print('salaries', salaries)

# tax = 19%, I want to have net salaries
net_salaries = [round(salary * 0.81, 2) for salary in salaries]
print('net_salaries', net_salaries)

# if base salary is greater than 2000 we want to give 10% bonus of the base salary
bonuses = []
for salary in salaries:
    if salary > 2000:
        bonuses.append(0.1)
    else:
        bonuses.append(0.0)

print('bonuses', bonuses)
# (return if condition is true) if condition else (return if condition is false)
bonuses = [0.1 if salary > 2000 else 0.0 for salary in salaries]
print('bonuses', bonuses)

print(list(zip(net_salaries, bonuses)))

bonus_values = []
for salary, bonus in zip(net_salaries, bonuses):
    bonus_values.append(salary * bonus)

print(bonus_values)

bonus_values = [salary * bonus for salary, bonus in zip(net_salaries, bonuses)]
print(bonus_values)

to_pay_with_bonuses = [salary + bonus for salary, bonus in zip(net_salaries, bonus_values)]
print(to_pay_with_bonuses)

print('-' * 30)

cities = ['Warszawa', 'Kraków', 'Gdansk', 'Gdynia', 'Grodzisk']

g_cities = []
for city in cities:
    if city.startswith('G'):
        g_cities.append(city)

print(g_cities)

g_cities = [city for city in cities if city.startswith('G')]
print(g_cities)
