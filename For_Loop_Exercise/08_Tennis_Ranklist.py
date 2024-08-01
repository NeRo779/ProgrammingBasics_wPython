import math

W = 2000
F = 1200
SF = 720

tournaments_num = int(input())
starting_points = int(input())

gained_points = 0
total_wins = 0

for _ in range(tournaments_num):
    result = input()
    if result == "W":
        gained_points += W
        total_wins += 1
    elif result == "F":
        gained_points += F
    elif result == "SF":
        gained_points += SF

total_points = starting_points + gained_points
average_points = math.floor(gained_points / tournaments_num)
percent_won_tournaments = total_wins / tournaments_num * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_won_tournaments :.2f}%")

