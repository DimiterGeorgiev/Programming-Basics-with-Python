screening_type = input()
rows = int(input())
columns = int(input())

incomes = 0
cinema_capacity = rows * columns
price = 0
if screening_type == 'Premiere':
    price = 12
elif screening_type == 'Normal':
    price = 7.5
elif screening_type == 'Discount':
    price = 5
incomes = cinema_capacity * price
print(f'{incomes:.2f} leva')
