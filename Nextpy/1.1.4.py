import functools


def do_it(number, number2):
    print(number,number2)
    return int(number)+int(number2)


def sum_of_digits(number):
    return functools.reduce(do_it, str(number))


if __name__ == "__main__":
    print(sum_of_digits(104))
    print(sum_of_digits(3))


