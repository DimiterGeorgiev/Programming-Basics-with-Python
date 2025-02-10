import sys

inpt = input()
bigest = -sys.maxsize

while inpt != 'Stop':
    curr = int(inpt)
    if curr > bigest:
        bigest = curr
    inpt = input()
print(bigest)
