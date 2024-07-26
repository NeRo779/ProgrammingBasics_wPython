import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_break = break_duration * (1/8)
relax_time = break_duration * (1/4)

rest_time = break_duration - lunch_break - relax_time
needed_time = episode_duration - rest_time

if rest_time >= episode_duration:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(-needed_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(needed_time)} more minutes.")

