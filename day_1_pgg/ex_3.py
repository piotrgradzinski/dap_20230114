"""
Write a program to check if the number given by the user is:
- greater than 10
- less than or equal 15
- divisible by 2 (use the modulus operator)

Sample program output:
Enter the number: 15
Greater than 10: True
Less than or equal 15: True
Divisible by 2: False
"""

number = int(input('Enter the number: '))

print(f'Greater than 10: {number > 10}')
print(f'Less than or equal 15: {number <= 15}')
print(f'Divisible by 2: {number % 2 == 0}')

