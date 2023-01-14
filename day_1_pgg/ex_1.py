"""
Write a program that will print your name and height on the console.
Use variables to store information about your name and height.

Sample program output:
First name: John
Height: 180
"""

# PEP-8 - Python code style guide - https://peps.python.org/pep-0008/
First_name = 'Piotr'
Height = 182

# not in line with Pep-8
# firstName = 'Piotr'
# FirstName = 'Piotr'
# FIRSTNAME = 'Piotr'

# first_name='Piotr'  # not in line with Pep-8

# pep-8 compliant
first_name = 'Piotr'
height = 182

# ways to display this information

# 1 way
print('First name: ' + first_name)
print('Height: ' + str(height))

# 2 way
print('First name:', first_name)  # print by default adds one space between the arguments when displays them
print('Height:', height)  # you don't have to convert arguments to string, print will do that for you

# 3 way
# f-string or formatted string
# it's an alternative to concatenating strings, it's easier to write and read
# it works with all the ways of creating string literals: ', ", ''', """
print('First name: first_name')  # no f-string
print(f'First name: {first_name}')
print(f'Height: {height}')  # conversion to string will be done automatically


print('First name: ' + first_name + ', your height: ' + str(height))

print(f'First name: {first_name}, your height: {height}')
