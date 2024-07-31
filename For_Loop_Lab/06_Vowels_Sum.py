text = str(input())
sum = 0

for character in text:
    if character == "a":
        sum += 1
    if character == "e":
        sum += 2
    if character == "i":
        sum += 3
    if character == "o":
        sum += 4
    if character == "u":
        sum += 5

print(sum)

