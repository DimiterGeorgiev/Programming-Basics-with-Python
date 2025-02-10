hour = int(input())
minutes = int(input())

minutes = minutes + 15
rest = minutes % 60
more_hours = minutes // 60
hour = hour + more_hours

if hour == 24:
    hour = 0
if rest < 10:
    print(f'{hour}:0{rest}')
else:
    print(f'{hour}:{rest}')
    