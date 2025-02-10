name = input()
points = float(input())
count = int(input())

for i in range(1, count + 1):
    actor = input()
    length = len(actor)
    curr_points = float(input())
    points += curr_points * length / 2
    if points > 1250.5:
        print(f'Congratulations, {name} got a nominee for leading role with {points:.1f}!')
        break

if points <= 1250.5:
    need_points = 1250.5 - points
    print(f'Sorry, {name} you need {need_points:.1f} more!')



