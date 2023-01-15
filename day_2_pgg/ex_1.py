"""
Write a program that will check the age of the person based on their year of birth.
Use hardcoded number for the current year.

Sample program output:
Enter year of birth: 1980
You are of legal age!

f(x) = x + 1
g(y) = y * 10

g(f(6)) -> 70
g(7)
70
"""

year_of_birth = int(input('Enter year of birth: '))
age = 2023 - year_of_birth

if age >= 18:
    print('You are of a legal age!')
else:
    print('You are NOT of a legal age!')
