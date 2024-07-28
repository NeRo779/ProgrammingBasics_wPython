degrees = int(input())
time = str(input())
Outfit = 0
Shoes = 0

if time == "Morning":
    if 10 <= degrees <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    if 18 < degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    if degrees >= 25:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
if time == "Afternoon":
    if 10 <= degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    if 18 < degrees <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    if degrees >= 25:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
if time == "Evening":
    if 10 <= degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    if 18 < degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    if degrees >= 25:
        Outfit = "Shirt"
        Shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")

