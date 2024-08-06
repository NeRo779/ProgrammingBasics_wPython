total_presentation_sum = 0
presentation_num = 0

judges_count = int(input())

command = input()
while not command == "Finish":
    current_presentation = command

    current_presentation_sum = 0
    for _ in range(judges_count):
        current_judge_score = float(input())
        current_presentation_sum += current_judge_score

    total_presentation_sum += current_presentation_sum
    presentation_num += 1

    average_score = current_presentation_sum / judges_count
    print(f"{current_presentation} - {average_score :.2f}.")

    command = input()

average_total_score = total_presentation_sum / (presentation_num * judges_count)
print(f"Student's final assessment is {average_total_score :.2f}.")

