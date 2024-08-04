start = int(input())
end = int(input())
magic_number = int(input())


combination_is_found = False
counter = 0
for first_number in range(start, end +1):
    for second_number in range(start, end + 1):
        counter += 1
        if first_number + second_number == magic_number:
            combination_is_found = True
            break

    if combination_is_found:
        break

if combination_is_found:
    print(f"Combination N:{counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")

