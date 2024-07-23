safety_nylon = 1.50
paint = 14.50
paint_thinner = 5.00
bag_price = 0.40

safety_nylon_needed = int(input())
paint_needed = int(input())
paint_thinner_needed = int(input())
hours_needed = int(input())

nylon_extra_needed = 2
paint_thinner_extra_needed = 0.10 * paint_needed

total_materials_amount = (safety_nylon_needed + nylon_extra_needed) * 1.50 \
    + (paint_needed + paint_thinner_extra_needed) * 14.50 \
    + (paint_thinner_needed * 5.00) \
    + bag_price

workers_price = (total_materials_amount * 0.30) * hours_needed

total_amount = total_materials_amount + workers_price

print(total_amount)

