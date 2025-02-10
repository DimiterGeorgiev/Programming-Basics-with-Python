command = input()

while command != 'End':
    destination = command
    full_money = float(input())
    sum_of_money = 0
    while sum_of_money < full_money:
        money = float(input())
        sum_of_money += money
    print(f'Going to {destination}!')

    command = input()
