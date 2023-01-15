# Conditional statements

country = input('Provide country name: ')

print(f'Calculating tax for {country}')

if country == 'pl':
    print('Taxes for Poland are ... ')
elif country == 'de':
    print('Taxes for Germany are ... ')
elif country == 'fr':
    print('Taxes for France are ... ')
else:
    print(f'Sorry, we don\'t know how to calculate tax for {country}')

# here we have 2 separate conditional blocks
if country == 'pl':
    print('Taxes for Poland are ... ')
else:
    print('Sorry...')

if country == 'de':
    print('Taxes for Germany are ... ')
elif country == 'fr':
    print('Taxes for France are ... ')
else:
    print(f'Sorry, we don\'t know how to calculate tax for {country}')

print('Thank you for using our services')
