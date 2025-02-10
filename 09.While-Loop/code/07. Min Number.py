import sys

inpt = input()

smallest = sys.maxsize

while inpt != 'Stop':
    curr = int(inpt)
    if curr < smallest:
        smallest = curr
    inpt = input()
print(smallest)
