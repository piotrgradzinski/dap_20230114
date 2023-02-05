# Functions

# function execution
print("Hello world!", "My name is Piotr")

# DRY - Don't Repeat Yourself


# First we need to define a function
def say_hi():
    print('Hi!')


# Then, we have to execute our function
say_hi()
say_hi()


def say_hi_to_someone(first_name, last_name):
    print(f'Hello {first_name} {last_name}')


say_hi_to_someone('Piotr', 'GG')

my_first_name = 'John'
my_last_name = 'Doe'
say_hi_to_someone(my_first_name, my_last_name)


def my_sum(a, b):
    return a + b


result = my_sum(2, 3)
print(result)

print(my_sum(10, 20))


# Documentation
# "a: int" - type hinting
# "-> int" - what data type function returns
def multiply(a: int, b: int) -> int:
    """
    Function is multiplying two provided numbers.
    :param a: First number to multiply
    :param b: Second number to multiply
    :return: Result of multiplying a by b
    """
    return a * b


print(multiply(2, 3))

print('-' * 30)

"""
- argument with default value must be placed after requirements without default value
"""
def packer(text, start='>>', end='<<'):
    return f'{start}{text}{end}'


# how we can provide arguments?
# 1. Provide them as positional arguments
print(packer('Hello world'))
print(packer('Hello world', '[['))
print(packer('Hello world', '[[', ']]'))

# 2. Named arguments
print(packer(text='Hello world'))
print(packer(text='Hello world', start='[['))
print(packer(text='Hello world', start='[[', end=']]'))
print(packer(end=']]', text='Hello world', start='[['))

# 3. Mix of positional and named arguments
# First we provide arguments in a positional way
# then we can provide named arguments (for them
# in any order we want)
print(packer('Hello world', end=']]'))
