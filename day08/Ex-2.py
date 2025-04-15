def prime_checker(number):
    is_prime_true = True
    for i in range(2, number):
        if number % i == 0:
            is_prime_true = False
    if is_prime_true:
        print("it's a prime number")
    else:
        print("it's not a prime number")

n = int(input("check this number: "))
prime_checker(number=n)