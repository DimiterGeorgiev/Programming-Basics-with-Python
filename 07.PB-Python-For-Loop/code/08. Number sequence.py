import sys

n = int(input())
min_num = sys.maxsize
max_num = -sys.maxsize
for i in range(1, n + 1):
    curr = int(input())
    if curr < min_num:
        min_num = curr
    if curr > max_num:
        max_num = curr
print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
