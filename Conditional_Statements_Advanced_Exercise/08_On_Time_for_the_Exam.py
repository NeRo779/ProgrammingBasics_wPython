exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_minutes = exam_hour * 60 + exam_minutes
arrival_time_minutes = arrival_hour * 60 + arrival_minutes

hour = 0
minute = 0

if arrival_time_minutes > exam_time_minutes:
    print("Late")
    if diff >= 60:
        print(f"{diff} minutes after the start")
    else:
        hour = abs(diff) // 60
        minute - abs(diff) % 60
        print(f"{hour}:{minute :02d} hours after the start")
elif diff >= 30:
    print("On time")
    if not diff == 0:
        print(f"{abs(diff)} minutes before the start")
else:
        print("Early")
        if diff > 60:
            print(f"{abs(diff)} minutes before the start")
        else:
            hour = abs(diff) // 60
            minute - abs(diff) % 60
            print(f"{hour}:{minute :02d} hours before the start")



