type_flowers = input()
num_flowers = int(input())
budget = int(input())

rose_price = 5.00
dahlia_price = 3.80
tulip_price = 2.80
narcissus_price = 3.00
gladiolus_price = 2.50

price = 0
discount = 0

if type_flowers == "Roses":
    price = rose_price
    if num_flowers > 80:
        discount = 0.10
if type_flowers == "Dahlias":
    price = dahlia_price
    if num_flowers > 90:
        discount = 0.15
if type_flowers == "Tulips":
    price = tulip_price
    if num_flowers > 80:
        discount = 0.15
if type_flowers == "Narcissus":
    price = narcissus_price
    if num_flowers < 120:
        discount = -0.15
if type_flowers == "Gladiolus":
    price = gladiolus_price
    if num_flowers < 80:
        discount = -0.20

total = num_flowers * price * (1 - discount)

if budget >= total:
    print(f"Hey, you have a great garden with {num_flowers} {type_flowers} and {budget - total :.2f} leva left.")
else:
    print(f"Not enough money, you need {total - budget :.2f} leva more.")

