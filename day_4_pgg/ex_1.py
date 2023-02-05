"""
Create a simple, function based calculator
1. Ask for 2 numbers
2. Ask for operation: (+, -, *, /)
3. Do the calculation and present results
"""

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


number_1 = float(input('Provide number 1: '))
number_2 = float(input('Provide number 2: '))
operation = input('Provide operation(+, -, *, /): ')

if operation == '+':
    result = add(number_1, number_2)
elif operation == '-':
    result = substract(number_1, number_2)
elif operation == '*':
    result = multiply(number_1, number_2)
elif operation == '/':
    result = divide(number_1, number_2)
else:
    print('Invalid operation.')
    exit(1)

print(f'{number_1}{operation}{number_2}={result}')
