len = int(input())
width = int(input())

cake_pieces_total = len * width
cake_pieces_left = cake_pieces_total

current_pieces = 0
command = 0

while True:
    command = input()
    if command == "STOP":
        break
    current_pieces = int(command)
    cake_pieces_left -= current_pieces
    if cake_pieces_left <= 0:
        break

if cake_pieces_left > 0:
    print(f"{cake_pieces_left} pieces are left.")
else:
    print(f"No more cake left! You need {-cake_pieces_left} pieces more.")

