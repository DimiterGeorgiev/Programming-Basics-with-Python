money = float(input())

rest_coin_count = 0

cent = int(money * 100)

while cent >= 200:
    cent -= 200
    rest_coin_count += 1

while cent >= 100:
    cent -= 100
    rest_coin_count += 1

while cent >= 50:
    cent -= 50
    rest_coin_count += 1

while cent >= 20:
    cent -= 20
    rest_coin_count += 1

while cent >= 10:
    cent -= 10
    rest_coin_count += 1

while cent >= 5:
    cent -= 5
    rest_coin_count += 1

while cent >= 2:
    cent -= 2
    rest_coin_count += 1

while cent >= 1:
    cent -= 1
    rest_coin_count += 1

print(rest_coin_count)

