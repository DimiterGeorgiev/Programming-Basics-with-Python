days = int(input())
room_type = input()
evaluation = input()

nights = days - 1
end_price = 0

room_price = 18
apartment_price = 25
pres_apartment_price = 35

price = 0
discount = 0
eval_positive = 0
eval_negative = 0

if room_type == 'room for one person':
    price = room_price
    discount = 0
elif room_type == 'apartment':
    price = apartment_price
    if days < 10:
        discount = 30
    elif 10 <= days <= 15:
        discount = 35
    elif days > 15:
        discount = 50
elif room_type == 'president apartment':
    price = pres_apartment_price
    if days < 10:
        discount = 10
    elif 10 <= days <= 15:
        discount = 15
    elif days > 15:
        discount = 20

if evaluation == 'positive':
    eval_positive = 25
elif evaluation == 'negative':
    eval_negative = 10

end_price = nights * price * (1 - discount/100) * (1 + eval_positive/100) * (1 - eval_negative/100)

print(f'{end_price:.2f}')
