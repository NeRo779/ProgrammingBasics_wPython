excursion_price = float(input())

puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

puzzle_num = int(input())
talking_doll_num = int(input())
teddy_bear_num = int(input())
minion_num = int(input())
truck_num = int(input())

total_price = puzzle_price * puzzle_num \
              + talking_doll_price * talking_doll_num \
              + teddy_bear_price * teddy_bear_num \
              + minion_price * minion_num \
              + truck_price * truck_num
toys = puzzle_num + talking_doll_num + teddy_bear_num + minion_num + truck_num

discount = 0

if toys >= 50:
    discount = 0.25 * total_price

won_money = total_price - discount

shop_rent = 0.10 * won_money
money_left = won_money - shop_rent

if money_left >= excursion_price:
    print(f"Yes! {money_left - excursion_price :.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price - money_left :.2f} lv needed.")

