pens_pack_price = 5.80
marker_pack_price = 7.20
detergent_price = 1.20


pens_pack_amount = int(input())
marker_pack_amount = int(input())
detergent = int(input())
discount_percent = int(input())

total = pens_pack_amount * pens_pack_price \
    + marker_pack_amount * marker_pack_price \
    + detergent * detergent_price

total_with_discount = total * (100 - discount_percent) / 100

print(total_with_discount)

