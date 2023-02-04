"""
Write a program that counts the number of occurrences of vowels (`a, e, i, o, u, y`) in the string given by the user.

1. Use input function to get the string from the user
2. Iterate over that string using for loop
3. Check if particular letter is in the list of vowels, if so, count the letter.

What we can do with uppercase letters?
1. We can add to the vowels list.
2. We can use .lower() method.
"""

user_input = input('Provide a string: ')

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
number_of_vowels = 0

for character in user_input.lower():
    if character in vowels:
        number_of_vowels += 1

print(f'String {user_input} contains {number_of_vowels} vowels.')
