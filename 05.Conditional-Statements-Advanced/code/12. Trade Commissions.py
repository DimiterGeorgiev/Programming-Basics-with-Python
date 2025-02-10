town = input()
volume = float(input())

commision = 5.5

if (town == 'Sofia' or town == 'Varna' or town == 'Plovdiv') and volume >= 0:
    if town == 'Sofia':
        if 0 <= volume <= 500:
            commision = 5
        elif 500 <= volume <= 1000:
            commision = 7
        elif 1000 <= volume <= 10000:
            commision = 8
        elif volume > 10000:
            commision = 12
    elif town == 'Varna':
        if 0 <= volume <= 500:
            commision = 4.5
        elif 500 <= volume <= 1000:
            commision = 7.5
        elif 1000 <= volume <= 10000:
            commision = 10
        elif volume > 10000:
            commision = 13
    elif town == 'Plovdiv':
        if 0 <= volume <= 500:
            commision = 5.5
        elif 500 <= volume <= 1000:
            commision = 8
        elif 1000 <= volume <= 10000:
            commision = 12
        elif volume > 10000:
            commision = 14.5
    price = volume * commision / 100
    print(f'{price:.2f}')
else:
    print('error')
