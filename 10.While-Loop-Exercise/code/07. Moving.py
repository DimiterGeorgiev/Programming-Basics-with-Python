a = int(input())
b = int(input())
c = int(input())

left_volume = a * b * c

command = input()

while True:
    if command == "Done":
        break
    left_volume -= int(command)
    if left_volume < 0:
        break
    command = input()

if command == 'Done':
    print(f'{left_volume} Cubic meters left.')

else:
    print(f'No more free space! You need {abs(left_volume)} Cubic meters more.')
