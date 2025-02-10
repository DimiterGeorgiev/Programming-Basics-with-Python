command = input()

all_standard = 0
all_student = 0
all_kid = 0

while command != 'Finish':
    movie = command
    full_places = int(input())
    type_of_ticket = input()

    all_ticket_current = 0

    type_student_count = 0
    type_standard_count = 0
    type_kid_count = 0

    while type_of_ticket != 'End':

        if type_of_ticket == 'student':
            type_student_count += 1
            all_student += 1
        elif type_of_ticket == 'standard':
            type_standard_count += 1
            all_standard += 1
        elif type_of_ticket == 'kid':
            type_kid_count += 1
            all_kid += 1

        all_ticket_current = type_student_count + type_standard_count + type_kid_count

        if all_ticket_current == full_places:
            break
        type_of_ticket = input()
    percent_full = all_ticket_current / full_places * 100
    print(f"{movie} - {percent_full:.2f}% full.")
    command = input()

all_ticket = all_student + all_standard + all_kid
percent_student = all_student / all_ticket * 100
percent_standard = all_standard / all_ticket * 100
percent_kid = all_kid / all_ticket * 100
print(f'Total tickets: {all_ticket}')
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")