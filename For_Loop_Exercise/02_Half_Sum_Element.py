import sys

max_num = -sys.maxsize
sum_numbers = 0

n = int(input())

for _ in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num

total = sum_numbers - max_num

if max_num == total:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    sum_others = sum_numbers - max_num
    print(f"Diff = {abs(max_num - total)}")

