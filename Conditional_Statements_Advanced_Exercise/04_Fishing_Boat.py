budget = int(input())
season = str(input())
fisherman_count = int(input())

rent = 0
discount = 0
extra_discount = 0

if season == "Spring":
    rent = 3000
if season == "Summer" or season == "Autumn":
    rent = 4200
if season == "Winter":
    rent = 2600

if fisherman_count <= 6:
    discount = 0.10
if 7 <= fisherman_count <= 11:
    discount = 0.15
if fisherman_count >= 12:
    discount = 0.25

if fisherman_count % 2 == 0 and season != "Autumn":
    extra_discount = 0.05

total = rent * (1 - discount) * (1 - extra_discount )

if budget >= total:
    print(f"Yes! You have {budget - total :.2f} leva left.")
else:
    print(f"Not enough money! You need {total - budget :.2f} leva.")

