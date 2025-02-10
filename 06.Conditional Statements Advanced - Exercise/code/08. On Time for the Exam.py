hour_exam = int(input())
minute_exam = int(input())
hour_come = int(input())
minute_come = int(input())

dif_hour = 0
dif_minute = 0

full_time_minute_exam = hour_exam * 60 + minute_exam
full_time_minute_coming = hour_come * 60 + minute_come

coming = ''

if full_time_minute_coming > full_time_minute_exam:
    coming = 'Late'
elif full_time_minute_coming + 30 < full_time_minute_exam:
    coming = 'Early'
else:
    coming = 'On time'

different = 0

if full_time_minute_coming > full_time_minute_exam:
    different = full_time_minute_coming - full_time_minute_exam
else:
    different = full_time_minute_exam - full_time_minute_coming

dif_hour = different // 60
dif_minute = different % 60

print(f'{coming}')

if coming == 'Late':
    if dif_hour == 0:
        print(f'{dif_minute} minutes after the start')
    elif dif_hour != 0:
        if dif_minute > 9:
            print(f'{dif_hour}:{dif_minute} hours after the start')
        else:
            print(f'{dif_hour}:0{dif_minute} hours after the start')
elif coming == 'Early':
    if dif_hour == 0:
        print(f'{dif_minute} minutes before the start')
    elif dif_hour != 0:
        if dif_minute > 9:
            print(f'{dif_hour}:{dif_minute} hours before the start')
        else:
            print(f'{dif_hour}:0{dif_minute} hours before the start')
elif coming == 'On time':
    if dif_hour == 0:
        print(f'{dif_minute} minutes before the start')
    elif dif_hour != 0:
        if dif_minute > 9:
            print(f'{dif_hour}:{dif_minute} hours before the start')
        else:
            print(f'{dif_hour}:0{dif_minute} hours before the start')

