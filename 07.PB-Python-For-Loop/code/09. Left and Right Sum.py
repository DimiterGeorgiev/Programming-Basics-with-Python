n = int(input())
left_sum = 0
right_sum = 0

for i in range(1, n + 1):
    curr = int(input())
    left_sum += curr
for i in range(n, 2 * n):
    curr = int(input())
    right_sum += curr
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    dif = abs(left_sum - right_sum)
    print(f'No, diff = {dif}')
