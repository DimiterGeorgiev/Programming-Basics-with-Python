fruit = input()
day = input()
quantity = float(input())

price = 0
is_valid = True

if (day == 'Saturday' or day == 'Sunday' or day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday')\
        and (fruit == 'banana' or fruit == 'apple' or fruit == 'orange' or fruit == 'grapefruit' or fruit == 'kiwi' or fruit == 'pineapple' or fruit == 'grapes'):
    if day == 'Saturday' or day == 'Sunday':
        if fruit == 'banana':
            price = 2.70 * quantity
            print(f'{price:.2f}')
        elif fruit == 'apple':
            price = 1.25 * quantity
            print(f'{price:.2f}')
        elif fruit == 'orange':
            price = 0.90 * quantity
            print(f'{price:.2f}')
        elif fruit == 'grapefruit':
            price = 1.60 * quantity
            print(f'{price:.2f}')
        elif fruit == 'kiwi':
            price = 3.00 * quantity
            print(f'{price:.2f}')
        elif fruit == 'pineapple':
            price = 5.60 * quantity
            print(f'{price:.2f}')
        elif fruit == 'grapes':
            price = 4.20 * quantity
            print(f'{price:.2f}')
    elif day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        if fruit == 'banana':
            price = 2.50 * quantity
            print(f'{price:.2f}')
        elif fruit == 'apple':
            price = 1.20 * quantity
            print(f'{price:.2f}')
        elif fruit == 'orange':
            price = 0.85 * quantity
            print(f'{price:.2f}')
        elif fruit == 'grapefruit':
            price = 1.45 * quantity
            print(f'{price:.2f}')
        elif fruit == 'kiwi':
            price = 2.70 * quantity
            print(f'{price:.2f}')
        elif fruit == 'pineapple':
            price = 5.50 * quantity
            print(f'{price:.2f}')
        elif fruit == 'grapes':
            price = 3.85 * quantity
            print(f'{price:.2f}')
else:
    print('error')

