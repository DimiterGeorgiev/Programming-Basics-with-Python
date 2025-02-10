import math

count = int(input())
points = int(input())

initial_points = points

count_W = 0

for i in range(1, count + 1):
    stage = input()
    if stage == 'W':
        points += 2000
        count_W += 1
    elif stage == 'F':
        points += 1200
    elif stage == 'SF':
        points += 720

average_points = (points - initial_points) / count
percent_W = count_W / count * 100

print(f'Final points: {points}')
print(f'Average points: {math.floor(average_points)} ')
print(f'{percent_W:.2f}%')
