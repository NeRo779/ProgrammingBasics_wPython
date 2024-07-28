month = input()
nights = int(input())

studio_price_per_night = 0
apartment_price_per_night = 0

if month == "May" or month == "October":
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if nights > 14:
        studio_price_per_night *= 0.70
    elif nights > 7:
        studio_price_per_night *= 0.95
elif month == "June" or month == "September":
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
    if nights > 14:
        studio_price_per_night *= 0.80
elif month == "July" or month == "August":
    studio_price_per_night = 76
    apartment_price_per_night = 77

if nights > 14:
    apartment_price_per_night *= 0.90

total_studio_price = studio_price_per_night * nights
total_apartment_price = apartment_price_per_night * nights

print(f"Apartment: {total_apartment_price :.2f} lv.")
print(f"Studio: {total_studio_price :.2f} lv.")

