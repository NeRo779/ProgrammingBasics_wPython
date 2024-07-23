pages_amount = int(input())
pages_per_hour = int(input())
days_amount = int(input())

total_hours = pages_amount // pages_per_hour
hours_per_day = total_hours / days_amount

print(hours_per_day)
