# comment starts with # sign
# everything after that sign is ignored by python
# We are executing print function.

# function definition
# f(x) = x + 1

# function execution
# f(5) -> 6
# function_name(argument value)

# g(a, b) = a + b
# g(1, 2) -> 3

print('Hello world!')  # prints something to standard output
print('Hey!', 'My name is Piotr')

# (built-in) Data types, literals

# string - str
print('Hello world!')  # string literal: 'Hello world!'
print("Hello world!")

# Numbers
# integer - int
print(10)

# float
print(3.14)
print(3.0)
print(3.)
print(0.5)
print(.5)

# we have the same value from the mathematical standpoint
# but we have DIFFERENT types!
print(3, type(3))
print(3.0, type(3.0))

# https://en.wikipedia.org/wiki/Scientific_notation
print(3E2)  # 3*10^2 = 3*100

print(10000000)
print(10_000_000)

# boolean - bool comes with two values only: True and False
# you have to start with capital T, F
print(True, type(True))
print(False, type(False))
# print(false)  # KO: Unresolved reference 'false'

# None - NoneType with only one value None
# null value, empty value
print(None, type(None))

print(10, type(10))  # int
print(10.0, type(10.0))  # float
print('10')  # string

print('---')

# Operators
# int, float
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)

# 0.1 as a decimal number can't be represented in binary system
print(0.1 * 3)  # 0.30000000000000004

print(10 // 3)  # 3 floor division
print(10 % 3)  # modulus, 1, 10 = 3 * 3 + 1 -> 1, rest of the division
print(10 ** 3)  # exponent operator, 10 to the power of 3, 10^3

# the operators we have in python also take into consideration
# data types that they are operate on...
# print('Hello' / 'world')  # exception is thrown, program stops, TypeError: unsupported operand type(s) for /: 'str' and 'str'

print('Hello' * 3)  # getting new string with Hello repeated 3 times
print('Hello' + 'world')  # concatenation, getting new string made of the two strings Hello and world connected

#     str     + int
# print('Hello' + 10)  # TypeError: can only concatenate str (not "int") to str
# str() function converts the provided value (int, float, etc.) to string
print('Hello' + str(10))

print('---')

# variables
# create a variable with name first_name and assign, put into it, literal/value 'Piotr'
first_name = 'Piotr'
shoe_number = 46
print(first_name, shoe_number)

shoe_number = 43.5
print(shoe_number)

print('---')

# how we can define strings literals?
print('Hello world!')
print("Hello world!")

print('''Hello
world''')

print("""One line
second line
third line
""")

# comment
# another comment
# yet another comment


# f-string
first_name = 'Piotr'
print(f'My name is {first_name}')

price = 10 * 3.12356
print(price)
print(f'Price: {price}')

# format specifier
# https://www.python.org/dev/peps/pep-0498/#format-specifiers
# https://docs.python.org/3.9/library/string.html#formatspec

print(f'Price: {price:.2f}')
print(f'Price: >{price:10.2f}<')
print(f'Price: >{price:<10.2f}<')
print(f'Price: >{price:^10.2f}<')
print(f'Price: >{price:_^10.2f}<')

