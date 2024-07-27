working_hours = int(input())
day_of_the_week = str(input())

if day_of_the_week == "Monday" and 10 <= working_hours <= 18:
    print("open")
elif day_of_the_week == "Tuesday" and 10 <= working_hours <= 18:
    print("open")
elif day_of_the_week == "Wednesday" and 10 <= working_hours <= 18:
    print("open")
elif day_of_the_week == "Thursday" and 10 <= working_hours <= 18:
    print("open")
elif day_of_the_week == "Friday" and 10 <= working_hours <= 18:
    print("open")
elif day_of_the_week == "Saturday" and 10 <= working_hours <= 18:
    print("open")
else:
    print("closed")

