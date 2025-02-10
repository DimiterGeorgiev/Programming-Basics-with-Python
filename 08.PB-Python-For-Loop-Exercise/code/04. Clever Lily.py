lily_alt = int(input())
wash_price = float(input())
toy_price = int(input())

sum_money = 0
curr_money = 10
cont_toy = 0

for i in range(1, lily_alt + 1):
    if i % 2 == 0:
        sum_money += curr_money - 1
        curr_money += 10
    else:
        cont_toy += 1

full_money = sum_money + cont_toy * toy_price
if full_money >= wash_price:
    rest_money = full_money - wash_price
    print(f'Yes! {rest_money:.2f}')
else:
    need_money = wash_price - full_money
    print(f'No! {need_money:.2f}')
