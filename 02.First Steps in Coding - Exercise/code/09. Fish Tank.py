l_cm = int(input())
b_cm = int(input())
h_cm = int(input())
procent = float(input())

voll = l_cm * b_cm * h_cm / 1000

vollEquipment = voll * procent/100

realVoll = voll - vollEquipment

print(realVoll)
