import math

n = int(input())
left_sum = 0
right_sum = 0

for i in range(0, n):
    left_side = float(input())
    left_sum += left_side

for i in range(0, n):
    right_side = float(input())
    right_sum += right_side

if left_sum == right_sum:
    print(f" Yes, sum = %d" % left_sum)
else:
    print(f" No, diff = %d " % math.fabs(right_sum - left_sum))

