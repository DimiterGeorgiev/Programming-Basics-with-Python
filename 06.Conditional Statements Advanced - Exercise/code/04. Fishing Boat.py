budge = int(input())
season = input()
count = int(input())

end_price = 0
price_boat = 0
discount_people = 0
discount_even = 0


if season == 'Spring':
    price_boat = 3000
elif season == 'Summer' or season == 'Autumn':
    price_boat = 4200
elif season == 'Winter':
    price_boat = 2600

if count <= 6:
    discount_people = 10
elif 7 <= count <= 11:
    discount_people = 15
elif count > 11:
    discount_people = 25

if count % 2 == 0 and season != 'Autumn':
    discount_even = 5

end_price = price_boat * (100 - discount_people)/100 * (100 - discount_even)/100

if end_price <= budge:
    rest_money = budge - end_price
    print(f'Yes! You have {rest_money:.2f} leva left.')
elif end_price > budge:
    need_money = end_price - budge
    print(f'Not enough money! You need {need_money:.2f} leva.')

