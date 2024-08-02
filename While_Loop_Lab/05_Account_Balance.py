total = 0
money = input()
while money != "NoMoreMoney":
    current_sum = float(money)
    if current_sum < 0:
        print(f"Invalid operation!")
        break
    print(f"Increase: {current_sum :.2f}")
    total += current_sum
    money = input()
print(f"Total: {total :.2f}")

