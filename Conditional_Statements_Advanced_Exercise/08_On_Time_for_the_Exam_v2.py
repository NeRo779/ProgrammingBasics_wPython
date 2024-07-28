exam_time_hours = int(input())
exam_time_minutes = int(input())
arrival_time_hours = int(input())
arrival_time_minutes = int(input())

total_exam_min = exam_time_hours * 60 + exam_time_minutes
total_arrival_min = arrival_time_hours * 60 + arrival_time_minutes

hours = 0
minutes = 0

diff = abs(total_exam_min - total_arrival_min)

if total_arrival_min > total_exam_min:
    print("Late")
    if diff >= 60:
        hours = diff // 60
        minutes = diff % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")
    else:
            print(f"{diff} minutes after the start")
elif total_arrival_min == total_exam_min:
    print("On time")

elif total_arrival_min < total_exam_min:
    if diff <= 30:
        print("On time")
        print(f"{diff} minutes before the start")
    else:
        if diff >= 60:
            hours = diff // 60
            minutes = diff % 60
            if minutes < 10:
                print("Early")
                print(f"{hours}:0{minutes} hours before the start")
            else:
                print("Early")
                print(f"{hours}:{minutes} hours before the start")
        else:
            print("Early")
            print(f"{diff} minutes before the start")

