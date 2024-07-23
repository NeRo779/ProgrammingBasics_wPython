deposit_amount = float(input()) #200
deposit_term = int(input()) #3
annual_interest_rate = float(input()) / 100  #5.7

final_amount = deposit_amount + deposit_term * ((deposit_amount * annual_interest_rate) / 12)

print(final_amount)
