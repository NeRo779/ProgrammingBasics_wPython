failed_grades = int(input())

failed_times = 0
solved_problems = 0
grades_count = 0
last_problem = ""
has_failed = True
grade = 0

while failed_times < failed_grades:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_count += grade
    solved_problems += 1
    last_problem = problem_name
if has_failed:
        print(f"You need a break, {failed_grades} poor grades.")
else:
        print(f"Average score: {grades_count / solved_problems :.2f}")
        print(f"Number of problems: {solved_problems}")
        print(f"Last problem: {last_problem}")

