budge = float(input())
season = input()

destination = ''
type_holiday = ''
price = 0
part_of_budge = 0

if budge <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        part_of_budge = 30
    elif season == 'winter':
        part_of_budge = 70
elif budge <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        part_of_budge = 40
    elif season == 'winter':
        part_of_budge = 80
elif budge > 1000:
    destination = 'Europe'
    part_of_budge = 90

if season == 'summer':
    type_holiday = 'Camp'
elif season == 'winter':
    type_holiday = 'Hotel'

if destination == 'Europe':
    type_holiday = 'Hotel'


price = budge * part_of_budge / 100

print(f'Somewhere in {destination}')
print(f'{type_holiday} - {price:.2f}')
