n = int(input())

sum_of_all_note = 0
counter = 0

command = input()

while command != 'Finish':
    name = command
    all_note_curr_name = 0
    for i in range(1, n + 1):
        curr_note = float(input())
        all_note_curr_name += curr_note
        sum_of_all_note += curr_note
        counter += 1
    average = all_note_curr_name / n
    print(f'{name} - {average:.2f}.')

    command = input()

finale_assessment = sum_of_all_note / counter

print(f'Student\'s final assessment is {finale_assessment:.2f}.')
