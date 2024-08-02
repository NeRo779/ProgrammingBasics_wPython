import sys

min_num = sys.maxsize
n = int(input())

while n != "Stop":
    num = int(n)
    if num < min_num:
        min_num = num
    n = input()
print(min_num)

