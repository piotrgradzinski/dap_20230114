# day_4_pgg/my_moduly.py

my_string = 'Hello world!'
my_list = [1, 2, 3, 4, 5]


def division(a: float, b: float) -> float:
    """
    Divides a by b.
    :param a:
    :param b:
    :return:
    """
    return a / b


# the following line will be executed when importing this module as well...
print('To bo or not to be!')

# the trick is...
if __name__ == '__main__':
    print('Mary had a little lamb...')
