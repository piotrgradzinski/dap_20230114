# How input function work?

print('Hello world!')  # sending data to standard output, so user can see it

# int() function converts something (in this case string) to integer (int).
height = int('182')  # we are assigning what int returned to variable height
print(height)

user_name = input('What is your name? ')
print(f'Your name, dear user is: {user_name}')

# input ALWAYS!!! returns string
# if we are expecting number, then we must convert
favourite_number = input('What is your favourite number? ')
print(favourite_number)
print(type(favourite_number))


favourite_number = int(favourite_number)
print(favourite_number)
print(type(favourite_number))

# int(input('What is your favourite number? '))
# int('44')
# favourite_number = 44
favourite_number = int(input('What is your favourite number? '))
print(favourite_number)
print(type(favourite_number))

number = float(input('Provide a float number: '))
print(number)
print(type(number))
