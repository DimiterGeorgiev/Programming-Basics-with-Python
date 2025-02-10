flowers = input()
count = int(input())
budget = int(input())

price = 0
rest_money = 0
need_money = 0
discount = 0
overprice = 0

if flowers == 'Roses':
    price = 5.00
    if count > 80:
        discount = 10
elif flowers == 'Dahlias':
    price = 3.80
    if count > 90:
        discount = 15
elif flowers == 'Tulips':
    price = 2.80
    if count > 80:
        discount = 15
elif flowers == 'Narcissus':
    price = 3.00
    if count < 120:
        overprice = 15
elif flowers == 'Gladiolus':
    price = 2.50
    if count < 80:
        overprice = 20

full_price = count * price * (100 - discount)/100 * (100 + overprice) / 100

if full_price > budget:
    need_money = full_price - budget
    print(f'Not enough money, you need {need_money:.2f} leva more.')
elif full_price <= budget:
    rest_money = budget - full_price
    print(f'Hey, you have a great garden with {count} {flowers} and {rest_money:.2f} leva left.')

