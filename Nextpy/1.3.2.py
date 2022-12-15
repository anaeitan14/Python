import functools

def is_prime(number):
    return functools.reduce(lambda result, other:result, [False if number % num == 0 else True for num in range(2, number)])


print(is_prime(42))
print(is_prime(43))
print(is_prime(3))