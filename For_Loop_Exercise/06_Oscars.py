actor_name = str(input())
starting_points = float(input())
judge_num = int(input())

total_points = starting_points
for _ in range(judge_num):
    judge_name = input()
    judge_points = float(input())
    total_points += (len(judge_name) * judge_points) / 2

    if total_points > 1250.5:
        break

if total_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points :.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - total_points :.1f} more!")

