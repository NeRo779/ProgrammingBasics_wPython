primes = 0
non_primes = 0

command = input()
while not command == "stop":
    number = int(command)

    if number < 0:
        print("Number is negative.")
        command = input()
        continue

    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            break

    if is_prime:
        primes += number
    else:
        non_primes += number

    command = input()

print(f"Sum of all prime numbers is: {primes}")
print(f"Sum of all non prime numbers is: {non_primes}")

