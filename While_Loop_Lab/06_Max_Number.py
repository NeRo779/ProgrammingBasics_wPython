import sys

max_num = -sys.maxsize
n = int(input())

while n != "Stop":
    num = int(n)
    if num > max_num:
        max_num = num
    n = input()
print(max_num)

