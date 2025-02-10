budget = float(input())
actors = int(input())
price = float(input())

dekor = budget * 0.1

kleid = actors * price

if actors > 150:
    kleid = kleid - kleid * 0.1

full_price = dekor + kleid

if budget < full_price:
    need_money = full_price - budget
    print(f'Not enough money!')
    print(f'Wingard needs {need_money:.2f} leva more.')
else:
    extra_money = budget - full_price
    print('Action!')
    print(f'Wingard starts filming with {extra_money:.2f} leva left.')


