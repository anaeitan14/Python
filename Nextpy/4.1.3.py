def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def first_prime_over(n):

    prime_generator = (number for number in range(n, n+100) if is_prime(number))

    return next(prime_generator)



if __name__ == "__main__":
    print(first_prime_over(1000000))