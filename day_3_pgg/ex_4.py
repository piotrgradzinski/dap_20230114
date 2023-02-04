"""
Write a program calculating the total amount due for the purchased goods based
on the weight and product name provided by the user.
To store price information per kilogram of the products use a dictionary.
List all available products in the store.

How we can do that?
1. Create a dictionary with products, lets add:
    potatoes - 1.2
    tomatoes - 4.5
    carrots - 0.5
2. Print the dictionary
3. Ask the user about the product and check if is available in our dictionary
4. Ask how many kilograms user wants to buy
5. Calculate users due
"""
products = {
    'potatoes': 1.2,
    'tomatoes': 4.5,
    'carrots': 0.5,
}

print('Available products:')
for product, price in products.items():
    print(f'{product} - {price:.2f}')

requested_product = input('Which product you would like to buy: ')

if requested_product not in products:
    print(f'The product you have requested is not available.')
    exit(1)  # exit returns a status code: 0 - everything is fine, other than 0 - something was wrong

weight = float(input(f'How many kilograms of {requested_product} would you like to buy: '))
amount_due = products[requested_product] * weight
print(f'For {weight} kg of {requested_product} you have to pay {amount_due:.2f}')
