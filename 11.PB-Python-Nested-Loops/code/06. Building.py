level = int(input())
room = int(input())

for e in range(level, 0, -1):
    for r in range(0, room):
        if e == level:
            print(f'L{e}{r} ', end="")
        elif e % 2 == 0:
            print(f'O{e}{r} ', end="")
        else:
            print(f'A{e}{r} ', end="")
    print("")
