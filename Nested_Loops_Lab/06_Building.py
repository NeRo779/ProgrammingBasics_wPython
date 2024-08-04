floors_num = int(input())
rooms_num = int(input())

floor_letter = ""

for current_floor in range(floors_num, 0, -1):
    if current_floor == floors_num:
        floor_letter = "L"
    elif current_floor % 2 == 0:
        floor_letter = "O"
    else: # current_floor % 2 != 0
        floor_letter = "A"

    for current_room in range(rooms_num): # range(0, rooms_num)
        print(f"{floor_letter}{current_floor}{current_room}",
end = " ")
    print()

