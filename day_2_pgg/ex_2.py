"""
Write a program that will calculate the result of the given operation
(adding, subtracting, multiplying, dividing) based on the two numbers given.
If an incorrect operation is specified, the program should display
an appropriate error message.

Sample program output:
Enter the first number: 10
Enter the second number: 5
Enter the type of operation (+, -, *, /): +
Result: 15
"""

number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
operation = input('Enter the type of operation (+, -, *, /): ')

if operation == '+':
    result = number_1 + number_2
elif operation == '-':
    result = number_1 - number_2
elif operation == '*':
    result = number_1 - number_2
elif operation == '/':
    result = number_1 / number_2
else:
    result = None

# for checking if value equals (is) None, True, False
# we should use "is" or "is not" operator
if result is None:
    print('Invalid operation')
else:
    print(f'{number_1}{operation}{number_2}={result}')
