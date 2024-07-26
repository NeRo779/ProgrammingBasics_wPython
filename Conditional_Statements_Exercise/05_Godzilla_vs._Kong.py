budget = float(input())
extras_num = int(input())
clothing_price = float(input())

movie_decor = 0.10 * budget
if extras_num > 150:
    clothing_price *= 0.90

money_needed = movie_decor + extras_num * clothing_price
money_left = budget - money_needed

# ~My Type
if money_needed > budget:
    print("Not enough money!")
    print(f"Wingard needs {money_needed - budget :.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_left :.2f} leva left.")
  
