max_count_bed_note = int(input())
inpt = input()
count_bed_note = 0
sum_of_all_note = 0
is_failed = False
count_of_all_note = 0
last_problem = ''

while inpt != 'Enough':
    last_problem = inpt
    note = int(input())
    sum_of_all_note += note
    count_of_all_note += 1
    if note <= 4:
        count_bed_note += 1
    if count_bed_note == max_count_bed_note:
        print(f'You need a break, {max_count_bed_note} poor grades.')
        is_failed = True
        break
    inpt = input()

if not is_failed:
    average_score = sum_of_all_note / count_of_all_note
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {count_of_all_note}')
    print(f'Last problem: {last_problem}')
