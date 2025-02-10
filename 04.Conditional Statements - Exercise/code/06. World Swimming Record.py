import math

record = float(input())
distance = float(input()) # meter
time_for_meter = float(input()) # seconds/meter

time = distance * time_for_meter

slower_mal = math.floor(distance / 15)

time_plus = slower_mal * 12.5

full_time = time + time_plus

if full_time < record:
    print(f'Yes, he succeeded! The new world record is {full_time:.2f} seconds.')
else:
    need_time = full_time - record
    print(f'No, he failed! He was {need_time:.2f} seconds slower.')

