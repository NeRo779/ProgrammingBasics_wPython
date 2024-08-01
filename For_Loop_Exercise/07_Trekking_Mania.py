musalla_climbers = 0
mont_blanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

total_groups = int(input())

for _ in range(total_groups):
    climbers = int(input())

    if climbers <= 5:
        musalla_climbers += climbers
    elif 6 <= climbers <= 12:
        mont_blanc_climbers += climbers
    elif 13 <= climbers <= 25:
        kilimanjaro_climbers += climbers
    elif 26 <= climbers <= 40:
        k2_climbers += climbers
    elif climbers >= 41:
        everest_climbers += climbers

total_climbers = musalla_climbers + mont_blanc_climbers + kilimanjaro_climbers + k2_climbers + everest_climbers

musalla_percent = musalla_climbers / total_climbers * 100
mont_blanc_percent = mont_blanc_climbers / total_climbers * 100
kilimanjaro_percent = kilimanjaro_climbers / total_climbers * 100
k2_percent = k2_climbers / total_climbers * 100
everest_percent = everest_climbers / total_climbers * 100


print(f"{musalla_percent :.2f}%")
print(f"{mont_blanc_percent :.2f}%")
print(f"{kilimanjaro_percent :.2f}%")
print(f"{k2_percent :.2f}%")
print(f"{everest_percent :.2f}%")

