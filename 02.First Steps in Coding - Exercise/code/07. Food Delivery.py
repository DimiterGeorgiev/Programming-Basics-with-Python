chiken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

price = chiken_menu * 10.35 + fish_menu * 12.40 + vegan_menu * 8.15
priceDesert = price * 0.2
fullPrice = price + priceDesert + 2.5

print(fullPrice)

