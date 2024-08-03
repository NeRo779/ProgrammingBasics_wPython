needed_money = float(input())
owned_money = float(input())

total_days = 0
spend_days = 0

total_money = owned_money
are_money_enough = False

while True:
    action = input()
    amount = float(input())
    total_days += 1

    if action == "spend":
        spend_days += 1
        total_money -= amount
        if total_money < 0:
            total_money = 0

        if spend_days >=5:
            break

    elif action == "save":
        spend_days = 0
        total_money += amount
        if total_money >= needed_money:
            are_money_enough = True
            break

if are_money_enough:
    print(f"You saved the money for {total_days} days.")
else:
    print(f"You can't save the money.")
    print(f"{total_days}")

