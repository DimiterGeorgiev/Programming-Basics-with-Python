inpt = input()
balance = 0
while inpt != "NoMoreMoney":
    amount = float(inpt)
    if amount < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {amount:.2f}')
    balance += amount
    inpt = input()
print(f'Total: {balance:.2f}')
