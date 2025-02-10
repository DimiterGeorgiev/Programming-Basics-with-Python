import math
form = input()
if form == 'square':
    a = float(input())
    area = a * a
elif form == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
elif form == 'circle':
    r = float(input())
    area = r * r * math.pi
elif form == 'triangle':
    a = float(input())
    h = float(input())
    area = a * h / 2
print(f"{area:.3f}")


