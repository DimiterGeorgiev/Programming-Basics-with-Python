n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(1, n + 1):
    curr = int(input())
    if curr < 200:
        p1 += 1
    elif 200 <= curr <= 399:
        p2 += 1
    elif 400 <= curr <= 599:
        p3 += 1
    elif 600 <= curr <= 799:
        p4 += 1
    else:
        p5 += 1
p1p = p1 / n * 100
p2p = p2 / n * 100
p3p = p3 / n * 100
p4p = p4 / n * 100
p5p = p5 / n * 100

print(f'{p1p:.2f}%')
print(f'{p2p:.2f}%')
print(f'{p3p:.2f}%')
print(f'{p4p:.2f}%')
print(f'{p5p:.2f}%')