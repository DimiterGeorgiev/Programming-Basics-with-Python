command = input()
all_step = 0
while True:
    if command == 'Going home':
        step = int(input())
        all_step += step
        break
    step = int(command)
    all_step += step
    if all_step >= 10000:
        break
    command = input()

if all_step < 10000:
    needed_step = 10000 - all_step
    print(f'{needed_step} more steps to reach goal.')
elif all_step >= 10000:
    step_over = all_step - 10000
    print(f'Goal reached! Good job!')
    print(f'{step_over} steps over the goal!')
