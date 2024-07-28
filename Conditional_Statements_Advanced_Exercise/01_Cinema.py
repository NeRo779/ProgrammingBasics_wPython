Premiere = 12.00
Normal = 7.50
Discount = 5.00

projection = str(input())
rows = int(input())
columns = int(input())
income = 0

capacity = rows * columns

if projection == "Premiere":
    income = capacity * 12.00
elif projection == "Normal":
    income = capacity * 7.50
elif projection == "Discount":
    income = capacity * 5.00

print(f"{income:.2f} leva")


