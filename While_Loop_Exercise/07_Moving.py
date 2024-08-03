width = int(input())
length = int(input())
height = int(input())

available_cubic_meters = width * length * height
cubic_meters_left = available_cubic_meters

current_space = 0

command = input()
while command != "Done":
    current_space = int(command)
    cubic_meters_left -= current_space
    if cubic_meters_left <= 0:
        break

    command = input()

if command == "Done":
    print(f"{cubic_meters_left} Cubic meters left.")
else:
    print(f"No more free space! You need {-cubic_meters_left} Cubic meters more.")

