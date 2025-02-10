command = input()

sum_non_prime = 0
sum_prime = 0

is_non_prime = False

while command != 'stop':
    current_num = int(command)
    if current_num < 0:
        print(f'Number is negative.')
    elif current_num == 0 or current_num == 1:
        sum_non_prime += current_num
    elif current_num == 2:
        sum_prime += current_num
    else:
        for i in range(2, current_num):
            if current_num % i == 0:
                is_non_prime = True
                break
        if is_non_prime:
            sum_non_prime += current_num
        else:
            sum_prime += current_num
        is_non_prime = False
    command = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')
