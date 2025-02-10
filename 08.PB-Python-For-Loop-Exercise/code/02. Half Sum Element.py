import sys

max_num = -sys.maxsize
sum_numbers = 0

n = int(input())

for i in range(1, n + 1):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num
if max_num == sum_numbers - max_num:
    sum_numbers -= max_num
    print(f'Yes')
    print(f'Sum = {sum_numbers}')
else:
    sum_numbers -= max_num
    dif = abs(max_num - sum_numbers)
    print('No')
    print(f'Diff = {dif}')
