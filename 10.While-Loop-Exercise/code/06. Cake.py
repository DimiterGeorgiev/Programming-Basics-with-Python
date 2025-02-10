a = int(input())
b = int(input())

all_pieces = a * b

pieces = 0

command = input()

while pieces < all_pieces:
    if command == 'STOP':
        break
    pieces += int(command)
    if pieces > all_pieces:
        break
    command = input()

if command == 'STOP':
    rest_pieces = all_pieces - pieces
    print(f'{rest_pieces} pieces are left.')

else:
    need_pieces = pieces - all_pieces
    print(f'No more cake left! You need {need_pieces} pieces more.')