def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2

    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        raise ValueError()


try:
    num1 = float(input('First number: '))
    num2 = float(input('Second number: '))
    operation = input('Operation (+, -, *, /): ')

    result = calculate(num1, num2, operation)
    print(f'{num1}{operation}{num2}={result}')
except ValueError:
    print('You have provided wrong value.')
