N1 = int(input())
N2 = int(input())
action = input()

result = 0

if action == '+' or action == '-' or action == '*':
    if action == '+':
        result = N1 + N2
    elif action == '-':
        result = N1 - N2
    elif action == '*':
        result = N1 * N2
    if result % 2 == 0:
        print(f'{N1} {action} {N2} = {result} - even')
    else:
        print(f'{N1} {action} {N2} = {result} - odd')
elif action == '/':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        result = N1 / N2
        print(f'{N1} {action} {N2} = {result:.2f}')
elif action == '%':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        result = N1 % N2
        print(f'{N1} {action} {N2} = {result}')




