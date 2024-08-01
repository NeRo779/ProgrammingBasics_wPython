num_tabs = int(input())
salary = int(input())

facebook = 150
instagram = 100
reddit = 50

for website in range(1, num_tabs + 1):
    current_tab = input()

    if current_tab == "Facebook":
        salary -= facebook
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif current_tab == "Instagram":
        salary -= instagram
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif current_tab == "Reddit":
        salary -= reddit
        if salary <= 0:
            print("You have lost your salary.")
            break

if salary > 0:
    print(salary)

