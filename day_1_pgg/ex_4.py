"""
Write a program to check if the number given by the user:
is odd, divisible by 3 and greater than 10
or
is the number 7

Sample program output:
Enter the number: 15
Result: True

Enter the number: 21
Result: True

Enter the number: 7
Result: True
"""

number = int(input('Enter the number'))

result = number > 10 or number == 7

print(result)
