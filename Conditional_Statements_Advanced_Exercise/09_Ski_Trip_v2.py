days = int(input()) - 1
room_type = input()
evaluation = input()

price = 0

if room_type == 'room for one person':
    price = 18
elif room_type == 'apartment':
    price = 25
    if days > 15:
        price *= 0.50
    elif days >= 10:
        price *= 0.65
    else:
        price *= 0.70
elif room_type == 'president apartment':
    price = 35
    if days > 15:
        price *= 0.80
    elif days >= 10:
        price *= 0.85
    else:
        price *= 0.90

if evaluation == 'positive':
    price *= 1.25
elif evaluation == 'negative':
    price *= 0.90

total_price = price * days

print(f'{total_price:.2f}')

