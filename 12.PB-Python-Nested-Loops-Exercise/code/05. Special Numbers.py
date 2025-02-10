n = int(input())

for number in range(1111, 9999):
    number_to_string = str(number)
    is_special = True
    for index, digit in enumerate(number_to_string):
        if int(digit) == 0:
            is_special = False
            break
        if n % int(digit) != 0:
            is_special = False
            break
    if is_special:
        print(number_to_string, end=" ")
