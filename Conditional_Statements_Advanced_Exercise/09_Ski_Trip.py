days = int(input())
room = input()
evaluation = input()

discount = 0
price = 0

if days < 10:
    if room == "room for one person":
        price = (days - 1) * 18
        if evaluation == 'positive':
            total = price + (price * 0.25)
        else:
            total = price - (price * 0.1)

    elif room == "apartment":
        price = (days - 1) * 25
        discount = price - (price * 0.3)
        if evaluation == "positive":
            total = discount + (discount * 0.25)
        else:
            total = discount - (discount * 0.1)

    elif room == "president apartment":
        price = (days - 1) * 35
        discount = price - (price * 0.1)
        if evaluation == "positive":
            total = discount + (discount * 25)
        else:
            total = discount - (discount * 0.1)

if 10 <= days <= 15:
    if room == "room for one person":
        price = (days - 1) * 18
        if evaluation == 'positive':
            total = price + (price * 0.25)
        else:
            total = price - (price * 0.1)

    elif room == "apartment":
        price = (days - 1) * 25
        discount = price - (price * 0.35)
        if evaluation == "positive":
            total = discount + (discount * 0.25)
        else:
            total = discount - (discount * 0.1)

    elif room == "president apartment":
        price = (days - 1) * 35
        discount = price - (price * 0.15)
        if evaluation == "positive":
            total = discount + (discount * 25)
        else:
            total = discount - (discount * 0.1)

if days > 15:
    if room == "room for one person":
        price = (days - 1) * 18
        if evaluation == 'positive':
            total = price + (price * 0.25)
        else:
            total = price - (price * 0.1)

    elif room == "apartment":
        price = (days - 1) * 25
        discount = price - (price * 0.5)
        if evaluation == "positive":
            total = discount + (discount * 25)
        else:
            total = discount - (discount * 0.1)

    elif room == "president apartment":
        price = (days - 1) * 35
        discount = price - (price * 0.2)
        if evaluation == "positive":
            total = discount + (discount * 25)
        else:
            total = discount - (discount * 0.1)


print(f"{price :.2f}")

