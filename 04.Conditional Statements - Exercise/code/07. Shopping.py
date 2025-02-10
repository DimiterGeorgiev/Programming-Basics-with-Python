budge = float(input())
count_videokart = float(input())
count_pocesors = float(input())
count_ram = float(input())

price_videkart = 250
price_procesor = price_videkart * count_videokart * 0.35
price_ram = price_videkart * count_videokart * 0.1

full_price = count_videokart * price_videkart + count_pocesors * price_procesor + count_ram * price_ram

if count_videokart > count_pocesors:
    full_price = full_price - full_price * 0.15

if budge >= full_price:
    rest_money = budge - full_price
    print(f'You have {rest_money:.2f} leva left!')
else:
    need_money = full_price - budge
    print(f'Not enough money! You need {need_money:.2f} leva more!')
