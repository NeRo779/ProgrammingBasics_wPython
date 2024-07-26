record_in_seconds = float(input())
distance = float(input())
seconds_per_one_meter = float(input())

resistance_seconds = distance // 15 * 12.50

total_time = distance * seconds_per_one_meter + resistance_seconds

if total_time < record_in_seconds:
    seconds_faster = record_in_seconds - total_time
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    seconds_slower = total_time - record_in_seconds
    print(f"No, he failed! He was {seconds_slower:.2f} seconds slower.")

