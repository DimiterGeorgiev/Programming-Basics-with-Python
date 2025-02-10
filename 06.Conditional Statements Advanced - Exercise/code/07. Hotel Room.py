month = input()
count = int(input())

end_price_apart = 0
end_price_studio = 0
price_apart = 0
price_studio = 0
discount_apart = 0
discount_studio = 0

if month == 'May' or month == 'October':
    price_studio = 50
    price_apart = 65
    if count > 14:
        discount_studio = 30
    elif count > 7:
        discount_studio = 5
elif month == 'June' or month == 'September':
    price_studio = 75.20
    price_apart = 68.70
    if count > 14:
        discount_studio = 20
elif month == 'July' or month == 'August':
    price_studio = 76
    price_apart = 77
    discount_studio = 0
    discount_apart = 0

if count > 14:
    discount_apart = 10

end_price_apart = price_apart * count * (1 - discount_apart / 100)
end_price_studio = price_studio * count * (1 - discount_studio / 100)

print(f'Apartment: {end_price_apart:.2f} lv.')
print(f'Studio: {end_price_studio:.2f} lv.')
