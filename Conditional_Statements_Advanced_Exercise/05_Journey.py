budget = float(input())
season = input()

destination = 0
place = 0
needed_money = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        needed_money = budget * 0.3
        place = "Camp"
    elif season == "winter":
        needed_money = budget * 0.7
        place = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        needed_money = budget * 0.4
        place = "Camp"
    elif season == "winter":
        needed_money = budget * 0.8
        place = "Hotel"
else:
    destination = "Europe"
    needed_money = budget * 0.9
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {needed_money:.2f}")

