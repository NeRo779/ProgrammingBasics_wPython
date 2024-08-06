student_tickets = 0
standard_tickets = 0
kids_tickets = 0
total_tickets = 0

command = input()
while not command == "Finish":
    movie_name = command
    free_seats = int(input())
    available_seats = free_seats

    while available_seats > 0:
        ticket_type = input()

        if ticket_type == "End":
            break

        available_seats -= 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1

    occupied_seats = free_seats - available_seats
    total_tickets += occupied_seats

    percent_space = occupied_seats / free_seats * 100
    print(f"{movie_name} - {percent_space :.2f}% full.")

    command = input()

percent_students = student_tickets / total_tickets * 100
percent_standards = standard_tickets / total_tickets * 100
percent_kids = kids_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_students :.2f}% student tickets.")
print(f"{percent_standards :.2f}% standard tickets.")
print(f"{percent_kids :.2f}% kids tickets.")

