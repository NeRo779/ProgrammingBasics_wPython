fee_for_one_year = int(input())
basketball_sneakers = fee_for_one_year * 0.60
basketball_outfit = basketball_sneakers * 0.80
basketball_ball = basketball_outfit * 0.25
basketball_accessories = basketball_ball * 0.20

fee_for_trainings = fee_for_one_year \
    + basketball_sneakers \
    + basketball_outfit \
    + basketball_ball \
    + basketball_accessories

print(fee_for_trainings)


