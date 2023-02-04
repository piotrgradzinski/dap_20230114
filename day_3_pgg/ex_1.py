"""
Write a program that counts occurrences of positive and negative
numbers in a given list of integers.
"""

# https://en.wikipedia.org/wiki/Negative_number
# zero is usually (but not always) thought of as neither positive nor negative

numbers = [1, 2, 3, -100, -10, 0, 4]

positive_numbers = 0
negative_numbers = 0

for number in numbers:
    if number > 0:
        positive_numbers += 1
    elif number < 0:
        negative_numbers += 1

print(f"Negatives: {negative_numbers}, positives: {positive_numbers}")
