destination = input()

current_money = 0
savings = 0

are_money_enough = False

while destination != "End":
    needed_budget = float(input())
    current_money = float(input())
    while current_money < needed_budget:
        savings = float(input())
        current_money += savings
    print(f"Going to {destination}!" )
    destination = input()

