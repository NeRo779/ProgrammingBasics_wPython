age = int(input())
price = float(input())
toy_price = int(input())

money = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        money += birthday * 10 / 2
        money -= 1
    else:
        money += toy_price

N = money - price
M = price - money

if money >= price:
    print(f"Yes! {N :.2f}")
else:
    print(f"No! {M :.2f}")

