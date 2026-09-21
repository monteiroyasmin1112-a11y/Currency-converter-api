import requests 
import time
#Start the Currency Converter using APIs
print('Welcome to the Currency Converter!')
print()
time.sleep(2)
continue_program = True
while continue_program:
    print('These are the currencies available in this app:')
    response = requests.get('https://api.frankfurter.dev/v2/currencies')
    data = response.json()
    currencies = []
    for currency in data:
        currencies.append(currency['iso_code'])
    print(currencies)
    print()
    while True:
        origin_currency = input('Enter the currency you want to convert from: ').upper()
        print()
        if origin_currency not in currencies:
            print('This currency doesn\'t exist')
            continue
        print('Valid currency')
        time.sleep(1)
        print('You have selected', origin_currency, 'as the currency to convert from.')
        print()
        break   
    while True:
        destination_currency = input('Enter the currency you want to convert to: ').upper()
        print()
        if destination_currency not in currencies:
                print('This currency doesn\'t exist')
                continue
        print('Valid currency')
        print('You have selected', destination_currency, 'as the currency to convert to.')
        print()
        break
    while True:
        try:
            enter_amount = float(input('Enter the amount you want to convert:').replace(',','.'))
            print()
        except ValueError:
            print('Please, enter a valid number.')
            continue
        time.sleep(1)
        print('You have entered', enter_amount, 'as the amount to convert.')
        print()
        break

    response = requests.get(f'https://api.frankfurter.dev/v2/rate/{origin_currency}/{destination_currency}')
    data = response.json()

    try: 
        rate = data['rate']
        converted_amount = enter_amount * rate
        time.sleep(1)
        print (f'Here is the Currency Converter result {converted_amount:.2f}')
    except KeyError:
        print('Currency not found. Please check the currency codes and try again')
        print()
    while True:
        user = input('Do you want to convert another currency?').upper()
        if user != 'YES' and user !='NO':
            print('invalid option!')
            print('Please,choose Yes or No.')
            print()
        elif user == 'YES':
            print('Going back to the main menu...')
            print()
            time.sleep(2)
        else:
            time.sleep(1)
            print('Closing Currency Converter...')
            continue_program = False 
            break


