name = input()
klass = 1
failed_count = 0
sum_note = 0

while klass < 13:
    note = float(input())
    if note > 3:
        klass += 1
        sum_note += note
    else:
        failed_count += 1
    if failed_count == 2:
        print(f'{name} has been excluded at {klass} grade')
        break

average = sum_note / 12
if failed_count != 2:
    print(f'{name} graduated. Average grade: {average:.2f}')

