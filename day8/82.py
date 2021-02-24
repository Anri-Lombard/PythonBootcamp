def prime_checker(number):
    if number > 1:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime:
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

    elif number < 0:
        print("Negative numbers cannot be prime numbers.")
    else:
        print(f"{number} is not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)