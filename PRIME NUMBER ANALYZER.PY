# Prime Number Analyzer

def is_prime(number):
    if number <= 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


def generate_primes(start, end):
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes


print("===== PRIME NUMBER ANALYZER =====")
print("1. Check whether a number is prime")
print("2. Generate prime numbers in a range")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    number = int(input("Enter a number: "))

    if is_prime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

elif choice == "2":
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    if start > end:
        print("Invalid range! Start must be less than or equal to end.")
    else:
        primes = generate_primes(start, end)

        if primes:
            print("Prime numbers:", primes)
            print("Total prime numbers:", len(primes))
        else:
            print("No prime numbers found in this range.")

else:
    print("Invalid choice! Please enter 1 or 2.")
