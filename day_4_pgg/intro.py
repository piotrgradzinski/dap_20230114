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
