chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery_price = 2.50

chicken_menu_amount = int(input())
fish_menu_amount = int(input())
vegan_menu_amount = int(input())

menu_price_total = chicken_menu_amount * chicken_menu \
    + fish_menu_amount * fish_menu \
    + vegan_menu_amount * vegan_menu

dessert_price = (0.20 * menu_price_total)

total_sum = menu_price_total + dessert_price + delivery_price

print(total_sum)
