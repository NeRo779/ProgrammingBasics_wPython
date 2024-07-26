budget = float(input())
video_card_num = int(input())
processor_num = int(input())
ram_num = int(input())
discount = 0

video_card_price = 250 * video_card_num
processor_price = (0.35 * video_card_price) * processor_num
ram_price = (0.10 * video_card_price) * ram_num

total_price = video_card_price + processor_price + ram_price

if video_card_num > processor_num:
    total_price = total_price - (total_price * 0.15)

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")

