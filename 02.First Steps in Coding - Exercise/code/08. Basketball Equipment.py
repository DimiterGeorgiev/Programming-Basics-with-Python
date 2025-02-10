taxes = int(input())

kecove = taxes - taxes * 0.4
equipment = kecove - kecove * 0.2
ball = equipment / 4
accessory = ball / 5

fullPrice = taxes + kecove + equipment + ball + accessory

print(fullPrice)