import math

name = input()
duration_movie = int(input())
duration_rest = int(input())

lunch_duration = duration_rest / 8
duration_pause = duration_rest / 4

duration_free_time = duration_rest - lunch_duration - duration_pause

if duration_free_time >= duration_movie:
    left_time = math.ceil(duration_free_time - duration_movie)
    print(f'You have enough time to watch {name} and left with {left_time} minutes free time.')
else:
    need_time = math.ceil(duration_movie - duration_free_time)
    print(f"You don't have enough time to watch {name}, you need {need_time} more minutes.")
